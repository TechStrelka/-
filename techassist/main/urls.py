from django.urls import path
from . import views


urlpatterns = [
    path('', views.registration),
    path('entr/', views.entr),
    path('profile/<pk>', views.profile.as_view())
]