from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Blog, Comment
from taggit.forms import TagField, TagWidget

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data


class PostForm(forms.ModelForm):
    tags = TagField(required=False, widget=TagWidget(attrs={'placeholder': 'Add tags separated by commas'}))

    class Meta:
        model = Blog
        fields = ['title', 'content', 'tags']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        post = super().save(commit=False)
        if self.user:
            post.author = self.user
        if commit:
            post.save()
            self.save_m2m()  # Save the tags
        return post


class PostUpdateForm(forms.ModelForm):
    tags = TagField(required=False, widget=TagWidget(attrs={'placeholder': 'Add tags separated by commas'}))

    class Meta:
        model = Blog
        fields = ['title', 'content', 'tags']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        post = super().save(commit=False)
        if self.user:
            post.author = self.user
        if commit:
            post.save()
            self.save_m2m()  # Save the tags
        return post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError("Content cannot be empty")
        return content
