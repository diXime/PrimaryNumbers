# -*- coding: utf-8 -*-
"""
MUSIC
Created on Mon Dec 05 02:26:13 2016

@author: Xiiime
"""
import sound
import pyaudio
import numpy as np

class Song() :
    def __init__(self):
        self.manifold = dict()
        self.suite = list()
        self.fs = 44100
        self.p = pyaudio.PyAudio()
    def playall(self):   
        stream = self.p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=self.fs,
                output=True,)
        # play. May repeat with different volume values (if done interactively) 
        volume=0.6
        for x in range(len(self.suite)):
            for y in range(len(self.suite[x].notes)):
                play=self.suite[x].notes[y]
                stream.write(volume*play)


        stream.stop_stream()
        stream.close()
        
        self.p.terminate()
        
    def addtoSuite(self, element):
        self.suite.append(element)            
        
    def looper(self,element,nombre=1):
        if type(nombre) is not int:
            return 'ParamError'
        else:
          for x in range(nombre):
                self.addtoSuite(element)
            
            
def Test():       
    print ('a=Song() <= Generates songmaker')    
    a=Song()    
    
    
    print('b=sound.Sound(param) <= call Sound from Song (Parameters of the sound in Sound, not in Song)')    
    #b=sound.Sound(volume=0.5,duration=0.3)
    print ('b.growtree(param) <= adds as a sound All the numbers up to param (here 680)')
    #b.growtree(680)
    print ('a.addtoSuite(b) <= When Sound b is made, a.addtoSuite to add to Song a')
    #a.addtoSuite(b)
    print('d=sound.Sound() <= Then create up any sound you want')
    d=sound.Sound()
    print ('d.connect to add a number to factorize in prime frequencies (core organ)')
    d.connect(300)
#    d.connect(293)
#    d.connect(392)
#    s.looper(d,3)
#    e=sound.Sound()
#    e.connect(261)
#    e.connect(293)
#    e.connect(440)
#    s.looper(e,3)
#    b=sound.Sound()
#    b.connect(261)
#    b.connect(293)
#    b.connect(415)
#    s.looper(b)
#    f=sound.Sound()
#    f.connect(261)
#    s.looper(f,7)
    print('a.addtoSuite(d) <= don t forget to add to suite ')
    a.addtoSuite(d)

    print('a.playall <= playing the whole suite added in Song...')
    a.playall()    
    return 'Nombre de notes : ', len(a.suite)