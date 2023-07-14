from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import LanguageSerializer, AuthorSerializer, PodcastSerializer, EpisodeSerializer
from .models import Language, Author, Podcast, Episode


class LanguageList(APIView):
    """
    List all languages, or create a new language
    """
    def get(self, request, format=None):
        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LanguageDetail(APIView):
    """
    Retrieve, update, or delete a Language instance
    """
    def get(self, request, pk, format=None):
        language = get_object_or_404(Language, pk=pk)
        serializer = LanguageSerializer(language)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        language = get_object_or_404(Language, pk=pk)
        serializer = LanguageSerializer(language)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        language = get_object_or_404(Language, pk=pk)
        language.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class AuthorList(APIView):
    """
    List all authors, or create a new author
    """
    def get(self, request, format=None):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AuthorDetail(APIView):
    """
    Retrieve, update, or delete an Author instance.
    """
    def get(self, request, pk, format=None):
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(author)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        author = get_object_or_404(Author, pk=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PodcastList(APIView):
    """
    List all podcasts, or create a new instance.
    """
    def get(self, request, format=None):
        podcasts = Podcast.objects.all()
        serializer= PodcastSerializer(podcasts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = PodcastSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PodcastDetail(APIView):
    """
    Retrieve, update, or delete a Podcast instance
    """
    def get(self, request, pk, format=None):
        podcast = get_object_or_404(Podcast, pk=pk)
        serializer = PodcastSerializer(podcast)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        podcast = get_object_or_404(podcast, pk=pk)
        serializer = PodcastSerializer(podcast, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)