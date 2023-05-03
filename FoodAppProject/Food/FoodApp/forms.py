from django import forms
from django.contrib.auth.models import User
class Userform(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name =  forms.CharField(max_length=100)
    username =   forms.CharField(max_length=100)
    password1 =  forms.CharField(max_length=100)
    ConfirmPassword =  forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)