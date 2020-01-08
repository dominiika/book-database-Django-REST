from rest_framework import serializers
from book import models
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )

        return user


class BookSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField('get_user')

    def get_user(self, obj):
        return obj.user.username

    def validate(self, data):
        isbn = data['isbn']
        isbn = isbn.replace('-', '')
        if len(isbn) != 13:
            raise serializers.ValidationError("The ISBN number must contain 13 digits!")
        if not isbn.isdigit():
            raise serializers.ValidationError("The ISBN number must contain only digits or \"-\"!")
        data['isbn'] = isbn
        return data

    class Meta:
        model = models.Book
        fields = ('id', 'author', 'publisher', 'title', 'isbn', 'published', 'user')
        extra_kwargs = {'user': {'read_only': True}}


class AuthorSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = models.Author
        fields = ('id', 'first_name', 'last_name', 'user')
        extra_kwargs = {'user': {'read_only': True}}


class PublisherSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = models.Publisher
        fields = ('id', 'name', 'established', 'user')
        extra_kwargs = {'user': {'read_only': True}}




