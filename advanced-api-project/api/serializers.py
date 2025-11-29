from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    publication_year = serializers.CharField(source='publication_year', =<2025=True) #it prevents user from requesting a book form the future

    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

  from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['name'] 

from rest_framework import serializers
from .models import Author, Book

class AuthrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

class BookSerializer(serializers.ModelSerializer):
    publication_year = publication_yearSerializer(=<2025=True , >2025=False) #it prevents user from requesting a book form the future

    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']
