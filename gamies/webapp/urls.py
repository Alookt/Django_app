from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.read, name = 'books'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]