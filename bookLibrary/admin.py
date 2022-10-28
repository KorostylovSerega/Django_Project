from django.contrib import admin
from .models import Genre, Author, Reader, Book

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Reader)
admin.site.register(Book)
