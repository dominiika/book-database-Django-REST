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
    re_path(r'^publishers/$', views.PublisherListView.as_view(), name='all-publishers'),
    re_path(r'^publishers/add/$', views.PublisherCreateView.as_view(), name='add-publisher'),
    re_path(r'^publishers/(?P<pk>\d+)/$', views.PublisherDetailView.as_view(), name='publisher-detail'),
    re_path(r'^publishers/(?P<pk>\d+)/edit/$', views.PublisherUpdateView.as_view(), name='update-publisher'),
    re_path(r'^publishers/(?P<pk>\d+)/delete/$', views.PublisherDeleteView.as_view(), name='delete-publisher'),
    re_path(r'^books/$', views.BookListView.as_view(), name='all-books'),
    re_path(r'^books/add/$', views.BookCreateView.as_view(), name='add-book'),
    re_path(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^books/(?P<pk>\d+)/edit/$', views.BookUpdateView.as_view(), name='update-book'),
    re_path(r'^books/(?P<pk>\d+)/delete/$', views.BookDeleteView.as_view(), name='delete-book'),
]
