from django.urls import path
from . import views
from .views import home

urlpatterns = [
path('', views.home, name="todo-home"),
path('add_todo/', views.add_todo),
path('delete_todo/<int:todo_id>/', views.delete_todo),
]
