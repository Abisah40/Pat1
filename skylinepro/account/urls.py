from django.urls import path
from .views import RegisterView,LoginView,PasswordResetView,PasswordResetConfirmView,PasswordVerifyView


urlpatterns = [
    path('register-user/', RegisterView.as_view(), name='register-user'),
    path('login-user/', LoginView.as_view(), name= 'login-user'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('reset-password-confirm/', PasswordVerifyView.as_view(), name='reset-password-confirm'),
    path('reset-password-complete/', PasswordResetConfirmView.as_view(), name='reset-password-complete'),
]