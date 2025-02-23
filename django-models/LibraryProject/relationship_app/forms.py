# relationship_app/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']  # List the fields you want in the form

    # You can also add custom validation if needed
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError("Title should be at least 3 characters long.")
        return title
