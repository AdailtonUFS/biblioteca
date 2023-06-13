from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'release_year', 'author_name', 'publisher', 'pages_quantity', 'created_at']
