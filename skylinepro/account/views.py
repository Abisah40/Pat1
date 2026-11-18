from django.shortcuts import render
from .models import User
from .serializers import CreateUserSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def Create_user(request):
    serializer = CreateUserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)