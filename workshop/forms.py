from django.forms import ModelForm
from django import forms
from .models import Workshop, Comment, Task, NewCategory
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class WorkShopForm(ModelForm):
    class Meta:
        model = Workshop
        fields = [
            'Name',
            'Category',
            'Description',
            'City',
            'StreetName',
            'ZipCode',
            'NIP'
        ]
        labels = {
            'Name':'Nazwa',
            'Category':'Kategoria',
            'Description':'Opis',
            'City':'Miasto',
            'StreetName':'Ulica',
            'ZipCode':'Kod pocztowy',
    }


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'Description',
            'Phone',
        ]
        labels = {
            'Description': 'Opis',
            'Phone': 'Numer Telefonu',
        }

class NewCategoryForm(ModelForm):
    class Meta:
        model = NewCategory
        fields = [
            'Description',
        ]
        labels = {
            'Description': 'Propozycja nowej kategorii',

        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'Comment',
            'Quality',
            'Price',
        ]
        labels = {
           'Comment':'Komentarz:',
            'Quality':'Jakość usług',
            'Price':'Cena usług',
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nazwa użytkownika:',
            'email': 'Adres email',
            'password1': 'Hasło ',
            'password2': 'Potwierdź hasło'
        }
