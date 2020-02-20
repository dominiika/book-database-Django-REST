from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^how-to/$', views.HowToUseApiView.as_view(), name='how-to-api'),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='all-authors'),
    re_path(r'^authors/add/$', views.AuthorCreateView.as_view(), name='add-author'),
    re_path(r'^authors/(?P<pk>\d+)/$', views.AuthorDetailView.as_view(), name='author-detail'),
    re_path(r'^authors/(?P<pk>\d+)/edit/$', views.AuthorUpdateView.as_view(), name='update-author'),
    re_path(r'^authors/(?P<pk>\d+)/delete/$', views.AuthorDeleteView.as_view(), name='delete-author'),
    re_path(r'^publishers/$', views.all_publishers, name='all-publishers'),
    re_path(r'^publishers/add/$', views.add_publisher, name='add-publisher'),
    re_path(r'^publishers/(?P<publisher_id>\d+)/$', views.publisher_detail, name='publisher-detail'),
    re_path(r'^publishers/(?P<publisher_id>\d+)/edit/$', views.update_publisher, name='update-publisher'),
    re_path(r'^publishers/(?P<publisher_id>\d+)/delete/$', views.delete_publisher, name='delete-publisher'),
    re_path(r'^books/$', views.all_books, name='all-books'),
    re_path(r'^books/add/$', views.add_book, name='add-book'),
    re_path(r'^books/(?P<book_id>\d+)/$', views.book_detail, name='book-detail'),
    re_path(r'^books/(?P<book_id>\d+)/edit/$', views.update_book, name='update-book'),
    re_path(r'^books/(?P<book_id>\d+)/delete/$', views.delete_book, name='delete-book'),
]
