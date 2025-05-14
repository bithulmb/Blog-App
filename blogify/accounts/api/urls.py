from django.urls import include,path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import RegisterUserView,CustomTokenObtainPairView

urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/user/register/', RegisterUserView.as_view(), name='custom-user-register'),
]
