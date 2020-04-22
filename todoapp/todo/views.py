from django.shortcuts import render
from .models import Todo_Objects
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    todo_items = Todo_Objects.objects.all().order_by("-added_date")
    # All of our to_do Todo_Objects


    return render(request, "todo/home.html", {"todo_items": todo_items})

def add_todo(request):
    current_date = timezone.now()  # Timezone object of the current time created
    content = request.POST["content"]  # Content from the form
    # print(added_date)
    # print(content)
    created_obj = Todo_Objects.objects.create(added_date=current_date, text=content)
    # print(created_obj)
    # print(created_obj.id)
    # return render(request, "todo/home.html")
    return HttpResponseRedirect("/")  # Redirect to home page
    # so that it our list gets updated when we add something

def delete_todo(request, todo_id):
    # Delete object
    Todo_Objects.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
