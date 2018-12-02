from django.contrib.auth.models import User
from .models import Page, Diary, Tag
from django.forms import ModelForm, Textarea, TextInput, PasswordInput
from django import forms


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
          'username': TextInput(attrs={'style': 'width: 74%'}),
          'email': TextInput(attrs={'style': 'width: 74%'}),
          'password': PasswordInput(attrs={'style': 'width: 74%'}),
        }
    

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'story', 'tag']
        widgets = {
          'story': Textarea(attrs={'rows':15, 'cols':60, 'style': 'width: 100%'}),
        }
