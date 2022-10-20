from django.urls import path, re_path

from .views import main, articles, archive, users, regexp

urlpatterns = [
    path('', main, name='main_page'),

    path('article/', articles, name='articles'),
    path('article/archive/', archive, name='archive'),
    path('users/', users, name='users'),

    path('article/<int:article_number>/', articles, name='articles_number'),
    path('article/<int:article_number>/archive/', archive, name='archive_number'),
    path('article/<int:article_number>/<slug:slug_text>/', articles, name='articles_slug'),
    path('users/<int:user_number>/', users, name='users_id'),

    re_path(r'^([1-9a-f]{4}\-[0-9a-zA-Z]{6})/$', regexp, name='regexp_slug'),
    re_path(r'^(0(39|67|68|96|97|98|50|66|95|99|63|73|93)\d{7})/$', regexp, name='regexp_phone')
]
