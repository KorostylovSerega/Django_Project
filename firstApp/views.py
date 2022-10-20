import string
from random import randrange, choices

from django.shortcuts import render


def main(request):
    data = {
        'article': randrange(1, 100),
        'slug': ''.join(choices(string.hexdigits, k=10))
    }
    return render(request, 'firstApp/index.html', data)


def articles(request, article_number=None, slug_text=None):
    data = {
        'article': article_number,
        'text': slug_text
    }
    return render(request, 'firstApp/articles.html', data)


def archive(request, article_number=None):
    return render(request, 'firstApp/archive.html', {
        'article': article_number
    })


def users(request, user_number=None):
    return render(request, 'firstApp/users.html', {
        'number': user_number
    })


def regexp(request, path, code=None):
    data = {
        'path': path,
        'code': code
    }
    return render(request, 'firstApp/regexp.html', data)
