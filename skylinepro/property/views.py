from django.shortcuts import render
from .models import CreateProperty
from .serializers import PropertySerializer
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework import generics
# Create your views here.

class Create_new_property(generics.CreateAPIView):
    queryset = CreateProperty.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [AllowAny]

class View_new_property(generics.ListAPIView):
    queryset = CreateProperty.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [AllowAny]

class update_property(generics.UpdateAPIView):
    queryset = CreateProperty.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [AllowAny]


class delete_property(generics.DestroyAPIView):
    queryset = CreateProperty.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [AllowAny]