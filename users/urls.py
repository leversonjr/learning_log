""" Define padroes de URL para users """

from django.urls import path
from django.contrib.auth.views import login

from . import views

urlpatterns= [
    #Pagina de login
    path('login/', login, {'template_name': 'users/login.html'}, name='login'),
    #Pagina de logout
    path('logout/', views.logout_view, name='logout'),
    # Pagina de cadastro
    path('register/', views.register, name='register'),
]