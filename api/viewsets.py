from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from api import serializers, permissions
from book import models
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    authentication_classes = (TokenAuthentication,)

    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email',)


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class BookViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.BookSerializer
    queryset = models.Book.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        IsAuthenticatedOrReadOnly,  # not authenticated users can only read
        permissions.UpdateOwnModel,  # only the creator can edit the book
    )

    filter_backends = (filters.SearchFilter,)
    search_fields = ('author', 'publisher', 'title', 'isbn', 'published', 'user')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AuthorViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.AuthorSerializer
    queryset = models.Author.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        permissions.UpdateOwnModel,
    )

    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name', 'user')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PublisherViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.PublisherSerializer
    queryset = models.Publisher.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        permissions.UpdateOwnModel
    )

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'established', 'user')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


