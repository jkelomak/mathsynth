#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 11:56:43 2018

@author: stobe
"""
#----Module description----

#The class Track holds all of the information about a piece. The initializing
#function parameters are: number of seconds per a bar, piece length in bars.
#compileTrack function writes a wav file with the name given as a parameter

import scipy.io.wavfile as wav
import numpy as np

#----Time functions----

#not to be called excessively
def mTime_to_rTime(mTime, secPerBar):
    return mTime*60/secPerBar

#not to be called excessively
def rTime_to_aTime(rTime):
    return 44100/rTime

#to be copied for necessary use
def mTime_to_aTime(mTime, secPerBar):
    if(mTime == 0):
        return 0
    return int(44100*mTime*secPerBar)
   
    
#----Track-class----

class Track:
    soundList = []
    
    def __init__(self, secPerBar, trackLen):
        self.secPerBar = secPerBar
        self.trackLen = trackLen
    
    def add(self, Snd):
        self.soundList.append(Snd)
    
    def compileTrack(self, filename):
        trk_l = mTime_to_aTime(self.trackLen, self.secPerBar)
        data = np.zeros(trk_l)
        for s in self.soundList:
            ss = s.toArray(self.secPerBar)
            data = np.concatenate([data[:ss[1]], data[ss[1]:ss[2]] + ss[0], data[ss[2]:]])
            
        wav.write(filename, 44100, data)
        

    