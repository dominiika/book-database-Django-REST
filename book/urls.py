from django.urls import path, re_path
from . import views

# https://www.codingforentrepreneurs.com/blog/how-django-urls-work-with-regular-expressions/

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    re_path(r'^$', views.IndexView.as_view(), name='index'),

    # path('how-to/', views.HowToUseApiView.as_view(), name='how-to-api'),
    re_path('^how-to/$', views.HowToUseApiView.as_view(), name='how-to-api'),

    # path('authors/', views.AuthorListView.as_view(), name='all-authors'),
    re_path('^authors/$', views.AuthorListView.as_view(), name='all-authors'),

    # path('authors/add/', views.AuthorCreateView.as_view(), name='add-author'),
    re_path('^authors/add/$', views.AuthorCreateView.as_view(), name='add-author'),

    # path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    re_path('^authors/(?P<pk>\d+)/$', views.AuthorDetailView.as_view(), name='author-detail'),

    # path('authors/<int:pk>/edit/', views.AuthorUpdateView.as_view(), name='update-author'),
    re_path('^authors/(?P<pk>\d+)/edit/$', views.AuthorUpdateView.as_view(), name='update-author'),

    path('authors/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='delete-author'),
    # path('^authors/(?P<pk>\d+)/delete/$', views.AuthorDeleteView.as_view(), name='delete-author'),

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
