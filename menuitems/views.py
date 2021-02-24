# from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Menu
from .serializers import MenuSerializer
# api list view

# from .serializers import TodoSerializer


class MenuListAPIView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuDetailAPIView(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
