from django.db import models
from django.contrib.auth.models import User


# class User(User):
#     name = models.CharField(max_length=50, null=False, default='Undef')
#     surname = models.CharField(max_length=50, null=False, default='Undef')
#     # username = models.CharField(max_length=50, null=False, default='Undef')
#     # email = models.CharField(max_length=100, null=False, default='Undef')
#     # password = models.CharField(max_length=100, null=False, default='Undef')
#     is_admin = models.BooleanField(null=False, default=False)

class Author(models.Model):
    name = models.CharField(max_length=50, null=False)
    surname = models.CharField(max_length=50, null=False)

class Genre(models.Model):
    name = models.CharField(max_length=50, null=False)

class Book(models.Model):
    name = models.CharField(max_length=100, null=False)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=False)
    publication_year = models.IntegerField(null=False)
    publisher = models.CharField(max_length=45, null=False)
    isbn = models.CharField(max_length=100, null=False)
    foto = models.CharField(max_length=100, default='nofoto')
    is_available = models.BooleanField(null=False)

class Book_Genre(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=False)