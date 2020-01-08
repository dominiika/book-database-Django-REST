from django.contrib import admin
from .models import Author, Publisher, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'user')


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'established', 'user')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'published', 'isbn', 'user')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)

