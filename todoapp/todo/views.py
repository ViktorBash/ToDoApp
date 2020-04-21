from django.shortcuts import render
from .models import Todo_Objects
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, "todo/home.html")
