from .models import user
from django.forms import ModelForm, TextInput, PasswordInput

class userform(ModelForm):
    class Meta:
        model = user
        fields = ['name', 'surname', 'login', 'password']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': "name"
            }),
            'surname': TextInput(attrs={
                'placeholder': "surname"
            }),
            'login': TextInput(attrs={
                'placeholder': "login"
            }),
            'password': TextInput(attrs={
                'placeholder': "password"
            })
        }


class entrform(ModelForm):
    class Meta:
        model = user
        fields = ['login', 'password']

        widgets = {
            'login': TextInput(attrs={
                'placeholder': "login"
            }),
            'password': TextInput(attrs={
                'placeholder': "password"
            })
        }