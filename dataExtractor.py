"""
This is a script written to extract some useful data from the data source

"""
import os
import glob
import hdf5_getters
import numpy as np
class Song:
    """
    This is a class to get the selected feature from a song in into a list which can be used as an array for further processing.
    """
    songCount = 0;
    def __init__(self):
        """
        A default function for self initilisation
        """
        Song.songCount += 1
        # Song.songDictionary[songID] = self
        self.artistID = []
        self.danceability = []
        self.duration = []
        self.similarity = []
        self.tempo = []
        self.year = []
        self.familiarity = []
        self.endoffade = []

    def movethroughfiles(self):
        """
        A function that moves through the database directory and allows to extract the feature from the directory.
        """
        basedir = "."
        ext = "H5"
        for root, dirs, files in os.walk(basedir):
            files = glob.glob(os.path.join(root, '*'+ext))
            for f in files:
                h5 = hdf5_getters.open_h5_file_read(f)
                self.artistID.append(hdf5_getters.get_artist_id(h5))
                self.danceability.append(hdf5_getters.get_danceability(h5))
                self.duration.append(hdf5_getters.get_duration(h5))
                self.similarity.append(hdf5_getters.get_similar_artists(h5))
                self.tempo.append(hdf5_getters.get_tempo(h5))
                self.year.append(hdf5_getters.get_year(h5))
                self.familiarity.append(hdf5_getters.get_artist_familiarity())
                self.endoffade.append(hdf5_getters.get_end_of_fade_in(h5))
                h5.close()

        
a = Song()
a.movethroughfiles()
b = np.array(a.artistID)
c = np.array(a.tempo)
print b
print c
