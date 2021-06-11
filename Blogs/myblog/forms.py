from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'desc', 'published', 'author']
        labels = {'title': 'Title', 'desc': 'Description', 'published': 'Published Date'}
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control bg-dark text-white'}),
                   'desc': forms.Textarea(attrs={'class': 'form-control bg-dark text-white'}),
                   'published': forms.TextInput(attrs={'class': 'form-control bg-dark text-white'})
                   }


class SignupForm(UserCreationForm):
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput(attrs={'class': 'form-control bg-dark text-white'}))
    password2 = forms.CharField(label="Confirm Password",
                                widget=forms.PasswordInput(attrs={'class': 'form-control bg-dark text-white'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control bg-dark text-white'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control bg-dark text-white'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control bg-dark text-white'}),
                   # 'username':forms.TextInput(attrs={'class':'form-control bg-dark text-white'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control bg-dark text-white'})
                   }


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'autocomplete': 'current-password', 'class': 'form-control bg-dark text-white'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autofocus': True, 'class': 'form-control bg-dark text-white'}))


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control bg-dark text-white'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control bg-dark text-white'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control bg-dark text-white'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control bg-dark text-white'})
                   }

