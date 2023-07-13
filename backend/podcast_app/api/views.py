from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import LanguageSerializer, AuthorSerializer
from .models import Language, Author, Podcast, Episode

class AuthorViewSet(ViewSet):
    """
    A ViewSet for listing or retrieving authors.
    """

    def list(self, request):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = AuthorSerializer(data=request.data)
        
        if serializer.is_valid():

            author = Author(**request.data)
            author.save()
            return Response(author, status=status.HTTP_201_CREATED)
        else:
            print("something went wrong")
            


    
    def retrieve(self, request, pk=None):
        queryset = Author.objects.all()
        author = get_object_or_404(queryset, pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)