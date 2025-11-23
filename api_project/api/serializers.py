from rest_framework import serializers
from .models import MyModel

class rest_framework(serializers.ModelSerializer):
    class BookSerializer:
        model = Book
        fields = ['title', 'author']
