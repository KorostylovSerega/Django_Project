from django.urls import path
from .views import book_library, book_reader

urlpatterns = [
    path('', book_library, name='library'),
    path('reader/<int:user_id>/', book_reader, name='Readers'),
]
