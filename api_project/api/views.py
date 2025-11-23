from django.shortcuts import render

from rest_framework import BookList
from .models import Book
from .serializers import BookSerializer

class rest_framework(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class rest_framework(viewsets.ModelViewSet):
     queryset = BookViewSet.objects.all()
     serializer_class = BookSerializer
