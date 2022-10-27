from datetime import timedelta

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone


class Users(models.Model):
    first_name = models.CharField('name', max_length=30)
    last_name = models.CharField('surname', max_length=30)
    nickname = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    registration_date = models.DateTimeField('registered', auto_now_add=True)

    class Meta:
        ordering = ['nickname']
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.nickname


class ArticlesCommentsInfo(models.Model):
    body = models.TextField('text')
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    publication_date = models.DateTimeField('published')
    comments = GenericRelation('comments')
    reactions = GenericRelation('response')

    class Meta:
        abstract = True


class Articles(ArticlesCommentsInfo):
    title = models.CharField(max_length=100)

    class Meta:
        ordering = ['title']
        verbose_name = 'article'
        verbose_name_plural = 'articles'

    def __str__(self):
        return self.title


class Comments(ArticlesCommentsInfo):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ['publication_date']
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.body

    def save(self, **kwargs):
        if not self.id:
            self.publication_date = timezone.now() - timedelta(days=365)
        super().save(**kwargs)


class Response(models.Model):
    LIKE = 'Y'
    DISLIKE = 'N'
    REACTION_CHOICES = [
        (LIKE, 'like'),
        (DISLIKE, 'dislike')
    ]
    reaction = models.CharField(max_length=1, choices=REACTION_CHOICES, default=LIKE)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        unique_together = ['author', 'content_type', 'object_id']
