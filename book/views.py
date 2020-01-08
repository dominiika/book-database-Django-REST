from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Publisher, Book
from .forms import AuthorModelForm, PublisherModelForm, BookModelForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404


def index(request):
    context = {}
    return render(request, 'book/index.html', context)


def all_authors(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'book/all-authors.html', context)


def author_detail(request, author_id):
    author = Author.objects.get(pk=author_id)
    books = Book.objects.filter(author=author)
    context = {'author': author, 'books': books}
    return render(request, 'book/author-detail.html', context)


@login_required(login_url="/account/login/")
def add_author(request):
    form = AuthorModelForm(request.POST or None)
    context = {'form': form, 'title': 'Add a new author'}
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            form.save()
            messages.success(request, "Author successfully created!")
            return redirect('/authors/')
        else:
            messages.error(request, "Author not successfully created")
    return render(request, 'book/form.html', context)


@login_required(login_url="/account/login/")
def update_author(request, author_id):
    author = Author.objects.get(pk=author_id)
    form = AuthorModelForm(request.POST or None, instance=author)
    context = {'form': form, 'author': author, 'title': f'Update the author called {author.first_name} {author.last_name}'}
    if author.user == request.user:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Author successfully edited!")
                return redirect(f'/authors/{author.id}/')
            else:
                messages.error(request, "Author not successfully edited")
        return render(request, 'book/form.html', context)
    else:
        raise Http404


@login_required(login_url="/account/login/")
def delete_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if author.user == request.user:
        if request.method == 'POST':
            author.delete()
            messages.success(request, "Author successfully deleted!")
            return redirect('/authors/')
        context = {'author': author, 'title': f'Do you want to delete the author called {author.first_name} {author.last_name}?'}
        return render(request, 'book/delete.html', context)
    else:
        raise Http404


def all_publishers(request):
    publishers = Publisher.objects.all()
    context = {'publishers': publishers}
    return render(request, 'book/all-publishers.html', context)


def publisher_detail(request, publisher_id):
    publisher = Publisher.objects.get(pk=publisher_id)
    books = Book.objects.filter(publisher=publisher)
    context = {'publisher': publisher, 'books': books}
    return render(request, 'book/publisher-detail.html', context)


@login_required(login_url="/account/login/")
def add_publisher(request):
    form = PublisherModelForm(request.POST or None)
    context = {'form': form, 'title': 'Add a new publisher'}

    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, "Publisher successfully created!")
            return redirect('/publishers/')
        else:
            messages.error(request, "Publisher not successfully created!")
    return render(request, 'book/form.html', context)


@login_required(login_url="/account/login/")
def update_publisher(request, publisher_id):
    publisher = Publisher.objects.get(pk=publisher_id)
    form = PublisherModelForm(request.POST or None, instance=publisher)
    context = {'form': form, 'publisher': publisher,
               'title': f'Update the publisher called {publisher.name}'}
    if publisher.user == request.user:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Publisher successfully edited!")
                return redirect(f'/publishers/{publisher.id}/')
            else:
                messages.error(request, "Publisher not successfully edited!")
        return render(request, 'book/form.html', context)
    else:
        raise Http404


@login_required(login_url="/account/login/")
def delete_publisher(request, publisher_id):
    publisher = get_object_or_404(Publisher, pk=publisher_id)

    if publisher.user == request.user:
        if request.method == 'POST':
            publisher.delete()
            messages.success(request, "Publisher successfully deleted!")
            return redirect('/publishers/')
        context = {'publisher': publisher, 'title': f'Do you want to delete the publisher called {publisher.name}?'}
        return render(request, 'book/delete.html', context)
    else:
        raise Http404


def all_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book/all-books.html', context)


def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {'book': book}
    return render(request, 'book/book-detail.html', context)


@login_required(login_url="/account/login/")
def add_book(request):
    form = BookModelForm(request.POST or None)
    context = {'form': form, 'title': 'Add a new book'}
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, "Book successfully created!")
            return redirect('/books/')
        else:
            messages.error(request, "Book not successfully created!")
    return render(request, 'book/form.html', context)


@login_required(login_url="/account/login/")
def update_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    form = BookModelForm(request.POST or None, instance=book)
    context = {'form': form, 'book': book,
               'title': f'Update the book called {book.title}'}
    if book.user == request.user:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Book successfully edited!")
                return redirect(f'/books/{book.id}/')
            else:
                messages.error(request, "Book not successfully edited!")
        return render(request, 'book/form.html', context)
    else:
        raise Http404


@login_required(login_url="/account/login/")
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if book.user == request.user:
        if request.method == 'POST':
            book.delete()
            messages.success(request, "Book successfully deleted!")
            return redirect('/books/')
        context = {'book': book, 'title': f'Do you want to delete the book called {book.title}?'}
        return render(request, 'book/delete.html', context)
    else:
        raise Http404


