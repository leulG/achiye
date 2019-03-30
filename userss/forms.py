from django import forms
from .models import JobOrder
from django.contrib.auth import (authenticate ,get_user_model ,login , logout)

user = get_user_model()
class UserRegistration(forms.ModelForm):
    email = forms.EmailField(label= 'email adress')
    email2 = forms.EmailField(label= 'confirm email adress')
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'confirm password' , widget=forms.PasswordInput)

    class Meta:
        model = user
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'email2',
            'password',
            ]
class UserJobOrder(forms.ModelForm):
    class Meta:
        model = JobOrder
        fields = [
            'Title',
            'File',
            'Description',

        ]
