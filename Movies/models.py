from django.db import models
from datetime import datetime

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    year = models.DateField()
    director = models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.title)
