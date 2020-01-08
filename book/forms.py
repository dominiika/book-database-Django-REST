from django import forms
from .models import Author, Publisher, Book


class AuthorModelForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('first_name', 'last_name')


class PublisherModelForm(forms.ModelForm):

    class Meta:
        model = Publisher
        fields = ('name', 'established')


class BookModelForm(forms.ModelForm):

    isbn = forms.CharField(label='ISBN:',
                           widget=forms.TextInput(attrs={'placeholder': '000-0-0000-0000-0'}))

    class Meta:
        model = Book
        fields = ('author', 'publisher', 'title', 'published', 'isbn')

    def clean_isbn(self, *args, **kwargs):
        isbn = self.cleaned_data.get("isbn")
        isbn = isbn.replace('-', '')
        if len(isbn) != 13:
            raise forms.ValidationError("The ISBN number must contain 13 digits!")
        if not isbn.isdigit():
            raise forms.ValidationError("The ISBN number must contain only digits or \"-\"!")
        return isbn
