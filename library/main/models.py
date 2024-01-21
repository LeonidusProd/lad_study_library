from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='users/', blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'

class Author(models.Model):
    name = models.CharField(max_length=50, null=False)
    surname = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f'{self.name} {self.surname}'

class Genre(models.Model):
    name = models.CharField(max_length=50, null=False)
    slug = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f'{self.name}'

class Book(models.Model):
    name = models.CharField(max_length=100, null=False)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=False)
    publication_year = models.IntegerField(null=False)
    publisher = models.CharField(max_length=45, null=False)
    isbn = models.CharField(max_length=100, null=False)
    foto = models.CharField(max_length=100, default='nofoto')
    is_available = models.BooleanField(null=False)

    def __str__(self):
        return f'{self.author.name}: {self.name}'

class Book_Genre(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f'{self.book}: {self.genre}'

class User_Reading(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)