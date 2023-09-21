""" Define padroes de urls para users """

# from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views


app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]
