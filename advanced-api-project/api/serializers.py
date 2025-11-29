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
    name = name(many=True , read_only=True)

    class Meta:
        model = Author
        fields = ['name'] 

from rest_framework import serializers
from .models import Author, Book

class AuthrSerializer(serializers.ModelSerializer):
    name = name(many=True , read_only=True)
    
    class Meta:
        model = Author
        fields = ['name']

class BookSerializer(serializers.ModelSerializer):
    publication_year = publication_yearSerializer(many=True , read_only=True) #it prevents user from requesting a book form the future

    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

def validate(self, data):
        if len(data['title']) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return data
