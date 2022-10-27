import datetime as dt
import random

from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.shortcuts import render

from .models import Articles, Comments, Users


def articles_view(request):
    data = {
        'articles': Articles.objects.all()
    }
    return render(request, 'blog/blog.html', data)


def get_last_comments(request):
    data = {
        'comments': Comments.objects.order_by('-publication_date')[:5]
    }
    return render(request, 'blog/last_comments.html', data)


def comments_updater(request):
    filter_comments = Comments.objects.filter(Q(body__contains='Middle') |
                                              Q(body__contains='Start') |
                                              Q(body__contains='Finish'))

    for comment in filter_comments:
        text = comment.body
        comment.body = f'{text} update on {dt.datetime.now()}'
        comment.save()

    data = {
        'comments': filter_comments
    }
    return render(request, 'blog/comments_update.html', data)


def comments_deleter(request):
    filter_comments = Comments.objects.filter(body__contains='k').exclude(body__contains='c')
    data = {
        'comments': filter_comments.delete()
    }
    return render(request, 'blog/comments_delete.html', data)


def last_two_comments(request):
    article = Articles.objects.order_by('-author__first_name').first()
    comments = article.comments.order_by('publication_date')[:2]
    data = {
        'article': article,
        'comments': comments
    }
    return render(request, 'blog/last_two_comments.html', data)


def comment_creator(request):
    author_id = random.choice([author.id for author in Users.objects.all()])
    article_id = random.choice([article.id for article in Articles.objects.all()])
    comment_text = 'simple comment'
    content_type = ContentType.objects.get(app_label='blog', model='articles')
    comment = Comments.objects.create(body=comment_text,
                                      author_id=author_id,
                                      content_type=content_type,
                                      object_id=article_id)
    comment.save()
    data = {
        'comment': comment
    }
    return render(request, 'blog/comment_create.html', data)
