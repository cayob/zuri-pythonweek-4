from django.db import models
from datetime import datetime

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField( max_length = 200)
    last_name = models.CharField(max_length = 200)
    age = models.IntegerField()

class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    date_of_release = models.DateField(default=datetime.today)
    likes = models.CharField
    artiste_id = models.CharField

class Lyric(models.Model):
    Song = models.ForeignKey(Song, on_delete = models.CASCADE)
    content = models.TextField()
    song_id = models.CharField
