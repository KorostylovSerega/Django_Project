from django.db import models


class Author(models.Model):
    first_name = models.CharField('name', max_length=30)
    last_name = models.CharField('surname', max_length=30)

    class Meta:
        ordering = ['first_name']
        verbose_name = 'author'
        verbose_name_plural = 'authors'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=30)
    year = models.PositiveSmallIntegerField()
    genre = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']
        verbose_name = 'book'
        verbose_name_plural = 'books'

    def __str__(self):
        return self.title


