from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('authors/', views.all_authors, name='all-authors'),
    path('authors/add/', views.add_author, name='add-author'),
    path('authors/<int:author_id>/', views.author_detail, name='author-detail'),
    path('authors/<int:author_id>/edit/', views.update_author, name='update-author'),
    path('authors/<int:author_id>/delete/', views.delete_author, name='delete-author'),

    path('publishers/', views.all_publishers, name='all-publishers'),
    path('publishers/add/', views.add_publisher, name='add-publisher'),
    path('publishers/<int:publisher_id>/', views.publisher_detail, name='publisher-detail'),
    path('publishers/<int:publisher_id>/edit/', views.update_publisher, name='update-publisher'),
    path('publishers/<int:publisher_id>/delete/', views.delete_publisher, name='delete-publisher'),

    path('books/', views.all_books, name='all-books'),
    path('books/add/', views.add_book, name='add-book'),
    path('books/<int:book_id>/', views.book_detail, name='book-detail'),
    path('books/<int:book_id>/edit/', views.update_book, name='update-book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete-book'),
]
