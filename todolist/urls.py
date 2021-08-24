
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #this is the index
    path('add', views.addTodoItem, name='add'),
    path('completed/<todo_id>', views.completedTodo, name='completed'),
    path('deleteCompleted', views.deleteCompleted, name='deleteCompleted'),
    path('deleteAll', views.deleteAll, name='deleteAll')
]