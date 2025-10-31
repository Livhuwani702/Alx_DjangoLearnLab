from django.db import models

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(mx_length=100)
  publication_year = models.IntField()
