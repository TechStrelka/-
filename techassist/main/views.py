from django.shortcuts import render, redirect
from .forms import userform, entrform
from .models import user
from django.views.generic import DetailView
def registration(request):
    error = ''
    if request.method == 'POST':
        login = request.POST['login']
        form = userform(request.POST)
        if login in user.objects.values_list('login', flat=True):
            error = ''
        if form.is_valid():
            form.save()
            return redirect(f'/profile/{login}')
        else:
            error = 'неверные данные'
    form = userform

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/registration.html', data)


def entr(request):
    error = ''
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        form = userform(request.POST)
        if login not in user.objects.values_list('login', flat=True):
            error = 'нет логина'
        else:
            password_user = user.objects.filter(login=login).values_list('password', flat=True).first()
            if str(password_user) != str(password):
                error = 'неверный пароль'
            else:
                return redirect(f'/profile/{login}')
    form = entrform

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/entr.html', data)


class profile(DetailView):
    model = user
    template_name = 'main/profile.html'
    context_object_name = 'user'

