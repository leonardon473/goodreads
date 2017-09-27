#Son mis cosas
from rest_framework import generics,filters
from .serializers import BookSerializer
from .models import Book
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

class ListBook(generics.ListCreateAPIView):# GET y POST
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = (filters.SearchFilter,DjangoFilterBackend)
    filter_fields = ('raiting','date_published','price','literary_genre')
    search_fields = ('title','prologue','literary_genre')
    permission_classes = (IsAuthenticated,)

class DetailBook(generics.RetrieveUpdateDestroyAPIView):# GET,PUT,DELETE,PATCH
    serializer_class = BookSerializer
    queryset = Book.objects.all() 