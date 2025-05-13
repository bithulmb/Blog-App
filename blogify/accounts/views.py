from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from .forms import LoginForm,RegisterForm

from django.contrib.auth import get_user_model

User = get_user_model()


class HomePageView(TemplateView):
    template_name = 'user_home.html'


class UserLoginView(TemplateView):
    template_name = 'user_login.html'


class UserRegisterView(TemplateView):
    template_name = 'user_register.html'


# class UserLoginView(FormView):
#     template_name = 'user_login.html'
#     form_class = LoginForm
#     success_url = reverse_lazy('home')

#     def form_valid(self, form):
#         login(self.request, form.user)
#         messages.success(self.request, "Logged in successfully!")
#         return super().form_valid(form)

# class UserRegisterView(CreateView):
#     template_name = 'user_register.html'
#     form_class = RegisterForm
#     success_url = reverse_lazy('login')

#     def form_valid(self, form):
#         messages.success(self.request, "Registration successful. Please login.")
#         return super().form_valid(form)


