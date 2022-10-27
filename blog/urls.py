from django.urls import path
from .views import articles_view, get_last_comments, comments_updater,\
    comments_deleter, last_two_comments, comment_creator

urlpatterns = [
    path('', articles_view, name='blog'),
    path('lastcomment/', get_last_comments, name='last_comment'),
    path('commentsupdates/', comments_updater, name='comments_update'),
    path('deletecomments/', comments_deleter, name='comments_delete'),
    path('lasttwocomments/', last_two_comments, name='last_two_comments'),
    path('commentcreate/', comment_creator, name='comment_create'),
]
