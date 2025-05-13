from django.urls import path,include
from .views import HomePageView,UserLoginView,UserRegisterView

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
   
   
]
