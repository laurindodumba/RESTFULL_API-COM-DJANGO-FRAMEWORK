from rest_framework import viewsets
from books.models import Book
from books.api import serializers

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BooksSerializer
    queryset = Book.objects.all()
