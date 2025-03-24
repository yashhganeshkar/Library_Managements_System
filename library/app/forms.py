from django import forms
from .models import AdminUser, Books
from django.contrib.auth.forms import UserCreationForm

class CreateNewBook(forms.ModelForm):
    class Meta:
        model = Books
        fields = [
            'title',
            'author',
            'isbn',
            'publish_date',
            'added_by'
        ]

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = AdminUser
        fields = ('username','email', 'password1', 'password2')