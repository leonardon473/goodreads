#Cosas de Django
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
#Cosas de DRF
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import generics,filters, status
#Mis cosas
from .serializers import BookSerializer
from .models import Book

class ListBook(generics.ListCreateAPIView):# GET y POST
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = (filters.SearchFilter,DjangoFilterBackend)
    filter_fields = ('raiting','date_published','price','literary_genre')
    search_fields = ('title','prologue','literary_genre')
    #permission_classes = (IsAuthenticated, )

class DetailBook(generics.RetrieveUpdateDestroyAPIView):# GET,PUT,DELETE,PATCH
    #permission_classes = (IsAuthenticated, )
    serializer_class = BookSerializer
    queryset = Book.objects.all() 

class UpdateBookCover(APIView):
    parser_classes = (FormParser, MultiPartParser)

    def handle_uploaded_file(self,f):
        path = "%s/%s" % (settings.MEDIA_ROOT,str(f))
        media = "%s/%s" % ("http://127.0.0.1:8000/media",str(f))  
        with open(path, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return media  

    def post(self,request,pk):
        try:
            media = self.handle_uploaded_file(request.FILES['file'])                        
            print(media)            
            try:
                book = Book.objects.get(pk=pk)
            except Book.DoesNotExist:
                raise Http404
            dic ={"cover":media}
            serializer = BookSerializer(book,data=dic, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)            
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_200_OK)