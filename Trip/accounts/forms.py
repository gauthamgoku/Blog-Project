from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import (authenticate,get_user_model)
from .models import Article_Comment
from . import models



class RegistrationForm(UserCreationForm):

    first_name = forms.CharField(max_length=254, required=False, help_text='Optional.')
    last_name  = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email      = forms.EmailField(max_length=254,required=True, help_text='Required. Inform a valid email address.')

    class Meta:
        model  =  User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)

class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(max_length=100)


class Register_User(forms.Form):

    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Article_Comment
        fields = ('username', 'article_comment',)

    