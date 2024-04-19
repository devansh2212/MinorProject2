from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm,self).__init__(*args,**kwargs)
        #Remove the default help text messages
        self.fields['password1'].help_text='The password length must be 8 characters'
        self.fields['password2'].help_text=''
        
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)