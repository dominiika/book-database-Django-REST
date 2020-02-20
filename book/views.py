from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Publisher, Book
from .forms import AuthorModelForm, PublisherModelForm, BookModelForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404

# CBV:
from django.views.generic import View, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.utils.decorators import method_decorator


class IndexView(View):

    def get(self, request, *args, **kwargs):
        try:
            books = Book.objects.all()[:3]
        except IndexError:
            books = Book.objects.all()
        try:
            authors = Author.objects.all()[:3]
        except IndexError:
            authors = Author.objects.all()
        try:
            publishers = Publisher.objects.all()[:3]
        except IndexError:
            publishers = Publisher.objects.all()

        context = {'books': books, 'authors': authors, 'publishers': publishers}
        return render(request, 'book/index.html', context)


class HowToUseApiView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'book/how-to-api.html')


class AuthorListView(ListView):
    model = Author
    template_name = 'book/all-authors.html'
    context_object_name = 'authors'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'book/author-detail.html'
    context_object_name = 'author'

    def get_object(self):
        obj = super().get_object()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.get_object()
        books = Book.objects.filter(author=author)
        context['books'] = books
        return context


@method_decorator(login_required, name='post')
@method_decorator(login_required, name='get')
class AuthorCreateView(CreateView):
    model = Author
    template_name = 'book/form.html'
    form_class = AuthorModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add a new author'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        messages.success(self.request, "Author successfully created!")
        return redirect('/authors/')

    def form_invalid(self, form):
        messages.error(self.request, "Author not successfully created")
        return render(self.request, 'book/form.html')


@method_decorator(login_required, name='post')
@method_decorator(login_required, name='get')
class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'book/form.html'
    form_class = AuthorModelForm
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Edit the author called {self.get_object()}'
        return context

    def form_valid(self, form):
        if self.get_object().user == self.request.user:
            form.instance.user = self.request.user
            form.save()
            messages.success(self.request, "Author successfully edited!")
            return redirect('/authors/')
        else:
            raise Http404

    def form_invalid(self, form):
        messages.error(self.request, "Author not successfully edited")
        return render(self.request, 'book/form.html')


@method_decorator(login_required, name='post')
@method_decorator(login_required, name='get')
class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'book/delete.html'
    success_url = '/authors/'
    context_object_name = 'author'
    success_message = "Author successfully deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AuthorDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise Http404
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Do you want to delete the author called {self.get_object()}?'
        return context


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


