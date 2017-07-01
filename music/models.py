"""Implementation of models from ERD"""

from django.db import models

# Create your models here.
class Song(models.Model):
    """
    This is table containg the list of song Name
    """

    song_title = models.CharField(max_length=250)

    def __str__(self):
        return self.song_title


class Album(models.Model):

    """
    This table contains Album, with Name and Year
    """
    Album_title = models.CharField(max_length=500)
    album_year = models.CharField(max_length=20)

    def __str__(self):
        return self.Album_title


class Artist(models.Model):
    """
    This is  Artist table, which has Artist's name
    """
    name = models.CharField(max_length=250)


class Keyword(models.Model):

    """
    This is a keyword that is used to identify the relation on table
    """
    word = models.CharField(max_length=250)

    def __str__(self):
        return self.word

class User(models.Model):
    """
    Contains the User table identifying the User.
    """
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    #username = models.CharField(max_length=30)
    email = models.EmailField(max_length=120,unique=True, db_index=True, primary_key=True)
    user_type = models.CharField(max_length=10)

    def __str__(self):
        return self.email

class Playlist(models.Model):
    """
    It contains a different songs that should be in a given Playlist
    """
    song_id = models.ManyToManyField(Song)

class UserPlaylist(models.Model):
    """
    It links to those playlist for individual user.
    """
    playlist_id = models.OneToOneField(Playlist, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Genre(models.Model):
    """
    A list of Genre for a given song.
    """
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class SongAlbum(models.Model):
    """
    This contains list of songs for a given album.
    """
    song_id = models.ManyToManyField(Song)
    album_id = models.OneToOneField(Album, on_delete=models.CASCADE)

class SongRating(models.Model):
    """
    It is a table for containing the rating for given song from multiple users.
    """
    rating = models.CharField(max_length=5)
    user_id = models.ManyToManyField(User)
    song_id = models.OneToOneField(Song, on_delete=models.CASCADE)

class SongArtist(models.Model):
    """
    Relates the number of songs for a given Artist
    """
    song_id = models.ManyToManyField(Song)
    artist_id = models.OneToOneField(Artist, on_delete=models.CASCADE)

class SongGenre(models.Model):
    """
    links to the Genre for given song
    """
    genre_id = models.ManyToManyField(Genre)
    song_id = models.OneToOneField(Song, on_delete=models.CASCADE)

class ArtistKeyword(models.Model):
    """
    Identifying Artist using keyword
    """
    keyword_id = models.ManyToManyField(Keyword)
    artist_id = models.OneToOneField(Artist, on_delete=models.CASCADE)

class SongKeyword(models.Model):
    """
    Identifying the song from given keyword
    """
    keyword_id = models.ManyToManyField(Keyword)
    song_id = models.OneToOneField(Song, on_delete=models.CASCADE)

class AlbumKeyword(models.Model):
    """
    Identifying albums from keyword
    """
    album_id = models.OneToOneField(Album, on_delete=models.CASCADE)
    keyword_id = models.ManyToManyField(Keyword)

class PlaylistKeyword(models.Model):
    """
    Identifying Playlist from keyword
    """
    playslist_id = models.OneToOneField(Playlist, on_delete=models.CASCADE)
    keyword_id = models.ManyToManyField(Keyword)

class RatingKeyword(models.Model):
    """
    Identifying Playlist from keyword
    """
    rating_id = models.OneToOneField(SongRating, on_delete=models.CASCADE)
    keyword_id = models.ManyToManyField(Keyword)
