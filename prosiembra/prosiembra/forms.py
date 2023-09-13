from typing import Any
from django import forms
from django.contrib.auth.models import User 

class RegisterForm(forms.Form):
    name = forms.CharField(required=True)
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, max_length=10, widget=forms.PasswordInput)
    confirm_password = forms.CharField (required=True, max_length=10, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuentra en uso')

        return username      

    def clean_email(self):
            email = self.cleaned_data.get('email')

            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('El email ya se encuentra en uso')

            return email    