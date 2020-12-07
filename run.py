# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 10:11:57 2020

@author: Jamie Burns
"""

from classes import *
import pickle
data = pd.read_csv('Data/data.csv')
MFCC = np.load('Data/mfcc.npy')
lib = Library(data, MFCC)

with open('Data/Library.obj', 'wb') as output:
    pickle.dump(lib, output, pickle.HIGHEST_PROTOCOL)
