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

from rest_framework.permissions import BasePermission

class IsAdminOrIsAdminUser(BasePermission):
    def has_permission(username, password, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user.is_staff
