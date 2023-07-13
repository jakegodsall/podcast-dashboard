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
    

