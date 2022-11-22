from django.urls import path
from todo.views import index, create, delet, edit

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delet/<int:pk>/', delet, name='delet'),
    
]
