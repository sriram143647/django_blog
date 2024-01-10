# yourapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BlogUser

class CustomUserCreationForm(UserCreationForm):
    # Add any additional fields or customization here
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    
    middle_name = forms.CharField(max_length=30) 
    contact_no = forms.CharField(max_length=10) 

    class Meta:
        model = BlogUser
        fields = UserCreationForm.Meta.fields + ('email','first_name','middle_name','last_name','contact_no',)