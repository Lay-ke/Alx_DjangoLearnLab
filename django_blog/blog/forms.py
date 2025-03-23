from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

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


# class UserUpdateProfileForm(forms.ModelForm):
#     photo = forms.ImageField(required=False)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name', 'photo']

#     def clean_photo(self):
#         photo = self.cleaned_data.get('photo')
#         if photo and not photo.content_type.startswith('image'):
#             raise forms.ValidationError("File type is not image")
#         return photo