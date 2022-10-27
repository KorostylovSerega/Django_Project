from django.shortcuts import render
from .models import Books, Readers


def book_library(request):
    data = {
        'books': Books.objects.all()
    }
    return render(request, 'bookLibrary/library.html', data)


def book_reader(request, user_id):
    data = {
        'reader': Readers.objects.get(id=user_id),
    }
    return render(request, 'bookLibrary/readers.html', data)
