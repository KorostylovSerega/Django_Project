from django.contrib import admin
from .models import Genres, Authors, Readers, Books

admin.site.register(Genres)
admin.site.register(Authors)
admin.site.register(Readers)
admin.site.register(Books)
