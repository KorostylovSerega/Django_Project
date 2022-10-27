from django.db import models


class Genres(models.Model):
    title = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

    def __str__(self):
        return self.title


class Authors(models.Model):
    first_name = models.CharField('name', max_length=30)
    last_name = models.CharField('surname', max_length=30)

    class Meta:
        ordering = ['first_name']
        verbose_name = 'author'
        verbose_name_plural = 'authors'
        unique_together = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Readers(models.Model):
    first_name = models.CharField('name', max_length=30)
    last_name = models.CharField('surname', max_length=30)
    email = models.EmailField(max_length=50, unique=True)

    class Meta:
        ordering = ['first_name']
        verbose_name = 'reader'
        verbose_name_plural = 'readers'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Books(models.Model):
    title = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    genres = models.ManyToManyField(Genres)
    authors = models.ManyToManyField(Authors)
    readers = models.ManyToManyField(Readers)
    availability = models.BooleanField(default=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'book'
        verbose_name_plural = 'books'

    def __str__(self):
        return self.title
