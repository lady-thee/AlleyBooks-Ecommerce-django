from django import forms 
from .models import Users, Profile


class UserForm(forms.Form):
    email = forms.EmailField(max_length=250, widget=forms.TextInput(attrs={
        'id': 'input',
        'name': 'email', 
        'placeholder': 'email',
        }))
    username = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'id': 'input',
        'placeholder': 'username',
        'name': 'username',
    }))
    fullname = forms.CharField(max_length=250, widget=forms.TextInput(attrs={
        'id': 'input',
        'placeholder': 'full names',
        'name': 'fullname', 
        'multiple': True,
    }))
    birthday = forms.DateField(widget=forms.DateInput(attrs={
        'id': 'input',
        'placeholder': 'birthday',
        'name': 'birthday', 
    }))
    location = forms.CharField(max_length=300, widget=forms.TextInput(attrs={
        'id': 'input',
        'placeholder': 'location',
        'name': 'location', 
    }))




class LoginForm(forms.Form):
    email = forms.EmailField(max_length=250, widget=forms.TextInput(attrs={
        'id': 'input',
        'name': 'email', 
        'placeholder': 'email',
        }))


class TokenForm(forms.Form):
    token = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'id': 'input',
        'placeholder': 'token from email',
        'name': 'token',
    }))
