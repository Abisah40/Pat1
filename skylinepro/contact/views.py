from django.shortcuts import render
from .serializers import ContactSerializer
from .models import ContactForm
from rest_framework import generics
from rest_framework.permissions import AllowAny

# Create your views here.


class CreateContact(generics.CreateAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

class ListContact(generics.ListAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

    #update contact view
class UpdateContact(generics.UpdateAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

    #delete contact view
class DeleteContact(generics.DestroyAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]
