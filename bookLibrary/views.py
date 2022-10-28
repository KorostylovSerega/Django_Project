from django.shortcuts import render
from .models import Book, Reader


def book_library(request):
    data = {
        'books': Book.objects.all()
    }
    return render(request, 'bookLibrary/library.html', data)


def book_reader(request, user_id):
    data = {
        'reader': Reader.objects.get(id=user_id),
    }
    return render(request, 'bookLibrary/readers.html', data)
