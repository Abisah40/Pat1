from .views import (CreateContact,ListContact)
from django.urls import path



urlpatterns = [
    #path('',CreateContact.as_view(), name= 'contactlist'),
    path('postcontact/',CreateContact.as_view(), name= 'contact-list'),
    path('viewcontact/',ListContact.as_view(), name= 'contact-view'),
]