from django.shortcuts import render

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from rest_framework import viewsets
from rest_framework import permissions
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class BookViewSet(viewsets.modelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

ListView, DetailView, CreateView, UpdateView, DeleteView

from django_filters import rest_framework
from rest_framework import generics

filters.OrderingFilter

filters.SearchFilter

title
author
publication_year
