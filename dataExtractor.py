"""
This is a script written to extract some useful data from the data source

"""
import os
import glob
import hdf5_getters
import numpy as np
class Song:
    songCount = 0;
    def __init__(self):
        Song.songCount += 1
        # Song.songDictionary[songID] = self
        self.artistID = []
        self.danceability = []
        self.duration = []
        self.genreList = []
        self.keySignature = []
        self.keySignatureConfidence = []
        self.similarity = []
        self.popularity = []
        self.tempo = []
        self.timeSignature = []
        self.timeSignatureConfidence = []
        self.year = []
        self.familiarity = []

    def movethroughfiles(self):
        basedir = "."
        ext = "H5"
        for root, dirs, files in os.walk(basedir):
            files = glob.glob(os.path.join(root, '*'+ext))
            for f in files:
                h5 = hdf5_getters.open_h5_file_read(f)
                self.artistID.append(hdf5_getters.get_artist_id(h5))
                h5.close()

    def Activate(self):
        self.movethroughfiles()
        
a = Song()
a.Activate()
b = np.array(a.artistID)
print b
