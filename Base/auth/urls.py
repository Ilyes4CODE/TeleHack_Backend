from django.urls import path
from . import views
from .views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
urlpatterns = [
    path('Sign_Up/',views.ClientRegisters),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('Profile/',views.Get_Profile),
    path('Logout/',views.logout)
]
