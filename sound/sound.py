# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 05:50:24 2016

@author: Xiiime

Produces regular beats (duration) of different chosen frequency(in a list notes[] ), 
whith primary numbers harmonics (Ut) 
"""

import numpy as np
import Ut as ut
import pyqtgraph as pg
# import matplotlib.pyplot as pl

        
class Sound():
    def __init__(self, volume=0.6, duration=0.7, frequency=60.0, framerate=44100):
        self.tree = ut.Ut()
        self.ut = ut.Ut()
        self.volume = volume
        self.notes= []
        self.fs = framerate
        self.duration = duration
        self.manifest = dict()
        # self.notes.append(sampler(duration,frequency))

    def sampler(self, frequency=130):
# SAMPLER
# Author:
# ivan_onys
# http://stackoverflow.com/questions/8299303/generating-sine-wave-sound-in-python
        fs = self.fs     # sampling rate, Hz, must be integer
        duration = self.duration   # in seconds, may be float
        f = frequency         # sine frequency, Hz, may be float
        if not isinstance(frequency, int):
            return frequency
        # handmade damper 
        if (f > 10000):
            f = np.sqrt(frequency)
        samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
        return samples    
        
        
    def addNote(self, frequency=0.0):
        self.notes.append(self.sampler(frequency))

    def addHarmonic(self,frequency, note=0, delay=0.0):
        if len(self.notes) == 0:
            self.sampler(frequency)
            return 'Added, not an harmonic: ', frequency
        else:
            if (type(frequency) == list) or isinstance(frequency, (list, tuple, np.ndarray)) :
                sampletoadd = frequency            
            else:
                sampletoadd = self.sampler(frequency)
            previoussample = self.notes[note-1]
            sample = np.multiply(sampletoadd, previoussample)
        self.notes[note]= sample
        return sample


    def connect(self, n):
        """
        Connecte un nombre à ses facteurs
        Arpeggiato
        """
        toout=list()
        self.manifest[n] = list()
        if not self.ut.tree:
            self.ut.treeme(n)
        if self.ut.checktree(n) == False:
            node = self.sampler(n)
            toout.append(node)  # Prime not in previous tree
        else:
            node= self.sampler(n)
            toout.append(node)  # Prime in tree
        w=0
        while w < len(self.ut.tree):
            if n % self.ut.tree[w] == 0 and n/self.ut.tree[w] != 1:
                premierfac = self.sampler(self.ut.tree[w]) # type="Prime"
                self.manifest[n].append(self.ut.tree[w])
                toout.append(premierfac)
                premierResultat = self.sampler(n/self.ut.tree[w]) # type="Factor"
                self.manifest[n].append(n/self.ut.tree[w])
                toout.append(premierResultat)
            elif n%self.ut.tree[w] == 0 and n/self.ut.tree[w] == 1 and n != 1:
                premierfac = self.sampler(n/self.ut.tree[w]) # type="Prime"
                self.manifest[n].append(n/self.ut.tree[w])
                toout.append(premierfac)
            w+=1
        if len(toout) != 0:
            #self.ut.tree[n] = toout
            note=np.array(toout[0])
            for x in range(len(toout)):
                
                self.addHarmonic(toout[x])               
                #self.notes.append(toout[x])
                
            self.notes.append(note)
#            pg.plot(self.notes[-1])          

    def growtree(self,value=0):
        self.tree.treeme(value)
        for x in range(len(self.tree.tree)):
           self.addNote(frequency = self.tree.tree[x])

    
    
    
    
    