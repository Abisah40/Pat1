from .views import (CreateContact,ListContact,UpdateContact,DeleteContact)
from django.urls import path



urlpatterns = [
    #path('',CreateContact.as_view(), name= 'contactlist'),
    path('post-contact/',CreateContact.as_view(), name= 'contact-list'),
    path('view-contact/',ListContact.as_view(), name= 'contact-view'),
    path('update-contact/<int:pk>/', UpdateContact.as_view(), name='contact-update'),
    path('delete-contact/<int:pk>/', DeleteContact.as_view(), name='contact-delete'),
]