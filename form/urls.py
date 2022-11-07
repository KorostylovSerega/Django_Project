from django.urls import path

from .views import english_level, authentication, user_page, logout_view, registration, change_password, comments_finder


urlpatterns = [
    path('', english_level, name='english_level'),
    path('login/', authentication, name='login'),
    path('user/', user_page, name='user'),
    path('logout/', logout_view, name='logout'),
    path('registration/', registration, name='registration'),
    path('change-password/', change_password, name='change_password'),
    path('comments/', comments_finder, name='comments'),
]
