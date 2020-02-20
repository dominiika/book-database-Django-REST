from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Publisher, Book
from .forms import AuthorModelForm, PublisherModelForm, BookModelForm
from django.contrib import messages
from django.http import Http404

# CBV:
from django.views.generic import View, ListView, DetailView, CreateView, DeleteView, UpdateView


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.get_object()
        books = Book.objects.filter(author=author)
        context['books'] = books
        return context


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
            # form.instance.user = self.request.user
            form.save()
            messages.success(self.request, "Author successfully edited!")
            return redirect('/authors/')
        else:
            raise Http404

    def form_invalid(self, form):
        messages.error(self.request, "Author not successfully edited")
        return render(self.request, 'book/form.html')


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


class PublisherListView(ListView):
    model = Publisher
    template_name = 'book/all-publishers.html'
    context_object_name = 'publishers'


class PublisherDetailView(DetailView):
    model = Publisher
    template_name = 'book/publisher-detail.html'
    context_object_name = 'publisher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        publisher = self.get_object()
        books = Book.objects.filter(publisher=publisher)
        context['books'] = books
        return context


class PublisherCreateView(CreateView):
    model = Publisher
    template_name = 'book/form.html'
    form_class = PublisherModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add a new publisher'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        messages.success(self.request, "Publisher successfully created!")
        return redirect('/publishers/')

    def form_invalid(self, form):
        messages.error(self.request, "Publisher not successfully created")
        return render(self.request, 'book/form.html')


class PublisherUpdateView(UpdateView):
    model = Publisher
    template_name = 'book/form.html'
    form_class = PublisherModelForm
    context_object_name = 'publisher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Edit the publisher called {self.get_object()}'
        return context

    def form_valid(self, form):
        if self.get_object().user == self.request.user:
            # form.instance.user = self.request.user
            form.save()
            messages.success(self.request, "Publisher successfully edited!")
            return redirect('/publishers/')
        else:
            raise Http404

    def form_invalid(self, form):
        messages.error(self.request, "Publisher not successfully edited")
        return render(self.request, 'book/form.html')


class PublisherDeleteView(DeleteView):
    model = Publisher
    template_name = 'book/delete.html'
    success_url = '/publishers/'
    context_object_name = 'publisher'
    success_message = "Publisher successfully deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PublisherDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise Http404
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Do you want to delete the publisher called {self.get_object()}?'
        return context


class BookListView(ListView):
    model = Book
    template_name = 'book/all-books.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book-detail.html'
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    template_name = 'book/form.html'
    form_class = BookModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add a new book'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        messages.success(self.request, "Book successfully created!")
        return redirect('/books/')

    def form_invalid(self, form):
        messages.error(self.request, "Book not successfully created")
        return render(self.request, 'book/form.html')


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book/form.html'
    form_class = BookModelForm
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add a new book'
        return context

    def form_valid(self, form):
        if form.instance.user == self.request.user:
            form.save()
            messages.success(self.request, "Book successfully edited!")
            return redirect('/books/')
        else:
            raise Http404

    def form_invalid(self, form):
        messages.error(self.request, "Book not successfully edited")
        return render(self.request, 'book/form.html')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book/delete.html'
    success_url = '/books/'
    context_object_name = 'book'
    success_message = "Book successfully deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BookDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise Http404
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Do you want to delete the book called {self.get_object()}?'
        return context
