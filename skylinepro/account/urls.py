from django.urls import path
from .views import Create_user


urlpatterns = [
    path('api-create-user/', Create_user,name='api-create-user'),
]