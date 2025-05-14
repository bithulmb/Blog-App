from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages


from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib.auth.views import LoginView

class UserSessionLoginView(LoginView):
    template_name = 'user_login.html'

class HomePageView(TemplateView):
    template_name = 'user_home.html'


class UserLoginView(TemplateView):
    template_name = 'user_login.html'


class UserRegisterView(TemplateView):
    template_name = 'user_register.html'



