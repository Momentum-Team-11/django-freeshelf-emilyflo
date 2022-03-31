from django import forms
from .models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'description',
            'URL',
            'favorited_by',
            'category'
        ]