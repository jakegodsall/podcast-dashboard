from rest_framework import serializers

from .models import Language, Author, Podcast, Episode

class LanguageSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return Language.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.save()
    #     return instance

class AuthorSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Author.objects.create(**validated_data)