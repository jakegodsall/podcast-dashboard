from rest_framework import serializers

from .models import Language, Author, Podcast, Episode

class LanguageSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)

    def validate_name(self, value):
        if Language.objects.filter(name=value).exists():
            raise serializers.ValidationError('Language must be unique.')
        return value

    def create(self, validated_data):
        """
        Create and return a new Language instance, given the validated data.
        """
        return Language.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Updata and return an existing Language instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class AuthorSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    
    def create(self, validated_data):
        """
        Create and return a new Author instance, given the validated data.
        """
        return Author.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing Author instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        instance.save()
        return instance
    

class PodcastSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    author = AuthorSerializer()
    language = LanguageSerializer()

    def create(self, validated_data):
        """
        Create and return a new Podcast instance, given the validated data.
        """
        return Podcast.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing Podcast instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.author = validated_data.get('author', instance.author)
        instance.language = validated_data.get('language', instance.language)

        instance.save()
        return instance
    

class EpisodeSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    episode_number = serializers.IntegerField(min_value=0)
    podcast = PodcastSerializer()
    duration = serializers.CharField(max_length=10)
    listen_link = serializers.URLField()
    in_new = serializers.BooleanField(default=False)

    def create(self, validated_data):
        """
        Create a new Episode instance, given the validated data.
        """
        return Episode.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing Episode instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.episode_number = validated_data.get('episode_number', instance.episode_number)
        instance.podcast = validated_data.get('podcast', instance.podcast)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.listen_link = validated_data.get('listen_link', instance.listen_link)
        instance.is_new = validated_data.get('is_new', instance.is_new)

        instance.save()
        return instance