from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import BlogUser

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'