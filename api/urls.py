from api import viewsets
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register('profile', viewsets.UserViewSet, basename='profile-api')
router.register('books', viewsets.BookViewSet, basename='books-api')
router.register('authors', viewsets.AuthorViewSet, basename='authors-api')
router.register('publishers', viewsets.PublisherViewSet, basename='publishers-api')


urlpatterns = [
    path('', include(router.urls)),
    path('login/', viewsets.UserLoginApiView.as_view()),

]
