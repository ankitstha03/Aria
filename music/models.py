from django.db import models

# Create your models here.
class Album(models.Model):
    Artist = models.CharField(max_length=250)
    Album_title  = models.CharField(max_length=500)
    Genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.Album_title + ' - ' + self.Artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
