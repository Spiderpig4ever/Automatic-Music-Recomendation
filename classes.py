import numpy as np
import pandas as pd
import os
import librosa
from tqdm import tqdm



#Functions to get mel-spectograms for a song
def get_audio_path( track_id):
    """
    Return the path to the mp3 given the directory where the audio is stored
    and the track ID.
    Examples
    --------
    >>> import utils
    >>> AUDIO_DIR = os.environ.get('AUDIO_DIR')
    >>> utils.get_audio_path(AUDIO_DIR, 2)
    '../data/fma_small/000/000002.mp3'
    """
    audio_dir = 'fma/data/fma_medium'
    tid_str = '{:06d}'.format(track_id)
    return os.path.join(audio_dir, tid_str[:3], tid_str + '.mp3')

def create_spectogram(track_id):
    filename = get_audio_path(track_id)
    y, sr = librosa.load(filename)
    spect = librosa.feature.melspectrogram(y=y, sr=sr,n_fft=2048, hop_length=1024)
    spect = librosa.power_to_db(spect, ref=np.max)
    return spect.T


class Library:
    def __init__(self, data, MFCC):
        #Create song library
        self.songs  = np.array([ Songs(row, MFCC[i]) for i, row in tqdm(data.iterrows())])
            
        
        
        
class Songs:
    def __init__ (self, row, mfcc):
        #Basic song information
        self.t_id = row.t_id
        self.label = row.label
        self.genre_name = row.genre_name
        
        #Songs features
        self.MEL = None
        self.MFCC = mfcc
        
        self.get_spectogram(self.t_id)
        
        
    def get_spectogram(self, t_id):
        spect = create_spectogram(t_id)
        spect = spect[:640, :]
        spect = librosa.core.db_to_power(spect)
        spect = np.log(spect)
        self.MEL = spect
    