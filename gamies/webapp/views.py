from django.shortcuts import render
from .models import Book

def index(request):
    books = Book.objects.all()
    for book in books:
        print({"title": book.Book_title, "published": book.published})
    return render(request, 'webapp/base.html', {"books": books})

def read(request):
    bookers = Book.objects.all()
    for b in bookers:
        print({"manuscript": b.manuscript})
    return render(request, 'webapp/books.html', {"books": bookers})