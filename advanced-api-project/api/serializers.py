from .models import Book, Author
from rest_framework import serializers

# Create a serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        if data['publication_year'] > 2025:
            raise serializers.ValidationError('Publication year must NOT be in the future')
        return data


# Create a serializer for the Author model
class AuthorSerializer(serializers.ModelSerializer):
    # Added a nested serializer for the books field to display the books associated with an author 
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']