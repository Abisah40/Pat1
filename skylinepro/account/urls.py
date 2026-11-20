from django.urls import path
from .views import RegisterView,LoginView,PasswordResetView,PasswordVerifyView,PasswordOTPView,PasswordResetRequestView


urlpatterns = [
    path('register-user/', RegisterView.as_view(), name='register-user'),
    path('login-user/', LoginView.as_view(), name= 'login-user'),
    path('reset-password-request/', PasswordResetRequestView.as_view(), name='reset-password-request'),
    path('reset-password-otp/', PasswordOTPView.as_view(), name='reset-password-confirm'),
    path('reset-password-change/', PasswordResetView.as_view(), name='reset-password-change'),
    path('verify-password-complete/', PasswordVerifyView.as_view(), name='verify-password'),
]