"""Implementation of models from ERD"""

from django.db import models

# Create your models here.
class keyword(models.Model):
    key_id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=250)
    pass

class user(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=120)
    user_type = models.CharField(max_length=10)
    user_id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.username

class user_playlist(models.Model):
    playlist_id = models.AutoField(primary_key=True)


class playslist(models.Model):
    playlist_id = models.AutoField(primary_key=True)
    song_id = models.CharField(max_length=50)

class song_keyword(models.model):
    this_id = models.foreignkey(keyword, on_delete=models.CASCADE)
    song_id= models.charfield(max_length=50)

class album_keyword(models.model):
    this_id = models.foreignkey(keyword, on_delete=models.CASCADE)
    album_id= models.charfield(max_length=50)

class artist_keyword(models.model):
    this_id = models.foreignkey(keyword, on_delete=models.CASCADE)
    artist_id= models.charfield(max_length=50)

class playlist_keyword(models.model):
    this_id = models.foreignkey(keyword, on_delete=models.CASCADE)
    playslist_id= models.charfield(max_length=50)

class rating_keyword(models.model):
    this_id = models.foreignkey(keyword, on_delete=models.CASCADE)
    rating_id= models.charfield(max_length=50)


class genre(models.model):
    this_id = models.foreignkey(keyword, on_delete=models.CASCADE)
    name = models.charfield(max_length=500)

class Song(models.Model):
    song_title = models.CharField(max_length=250)

    def __str__(self):
        return self.song_title

class Album(models.Model):
    album_id = models.CharField(max_length=250)
    Album_title = models.CharField(max_length=500)
    album_year = models.DateTimeField()

    def __str__(self):
        return self.Album_title + ' - ' + self.Artist

class song_album(models.Model):
    x_id = models.AutoField(primary_key=True)
    song_id = models.CharField(max_length=50)
    album_id = models.CharField(max_length=250)

class song_rating(models.Model):
    this_id = models.CharField(max_length=200)
    rating = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)

class song_artist(models.Model):
    this_id = models.CharField(max_length=200)
    song_id = models.CharField(max_length=50)
    artist_id = models.CharField(max_length=50)

class song_genre(models.Model):
    this_id = models.CharField(max_length=200)
    genre_id = models.CharField(max_length=50)
    artist_id = models.CharField(max_length=50)


