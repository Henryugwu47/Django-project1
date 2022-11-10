from datetime import datetime
from email.policy import default
from django.db import models

# Create your models here.
class Artiste(models.Model): 
  first_name = models.CharField(max_length=40)
  last_name = models.CharField(max_length=40)
  age = models.IntegerField()

  def __str__(self):
      return self.last_name

class Song(models.Model):
  Artiste = models.ForeignKey("Artiste", on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  date_released = models.DateField(default=datetime.today)
  likes = models.IntegerField()
  artist_id = models.IntegerField()

  def __str__(self):
      return self.title

class Lyric(models.Model):
  Song = models.ForeignKey("Song", on_delete=models.CASCADE)
  content = models.CharField(max_length=1000)
  song_id = models.IntegerField()

  def __str__(self):
      return self.Song
