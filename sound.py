#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 10:11:43 2018

@author: stobe
"""

#----Module description----

#The class Snd is to be subclassed by instruments (in their own module), 
#the instances of which create individual sounds. These instrument instances
#are to be added to the to the soundlist of the track with the add function. 

#Inputting frequency: There are two ways. One is to use the symbol # and follow
#it with the absolute frequency. The second, recommended way is to give the
#pitch as scientific notation with + substituting for sharp and - for flat.
#To use for example a just scale instead of equal-tempered, replace the parseFreq
#function in your instrument.

from abc import ABC, abstractmethod
import numpy as np

#---Utilities---

#mTime as in which bar and beat, aTime as in which array index
def mTime_to_aTime(mTime, secPerBar):
    if(mTime == 0):
        return 0
    return int(44100*mTime*secPerBar)

def parseFreq(freq):
    if '#' in freq:
        return int(freq[1:])
    def f(x):
        return {
            'C': 0,
            'D': 2,
            'E': 4,
            'F': 5,
            'G': 7,
            'A': 9,
            'B': 11,
        }[x]
    semitone = f(freq[0])
    freq = freq[1:]
    while freq[0] == '+':
        semitone += 1
        freq = freq[1:]
    while freq[0] == '-':
        semitone -= 1
        freq = freq[1:]
    if len(freq) != 1:
        print("parsing problems", freq)
    return 440*2**((semitone - 9 + (int(freq[0]) - 4) * 12)/12)
    

class Snd(ABC):
    #has properties ampArr, freqArr, waveform, freq, start, stop
    
    @abstractmethod
    def __init__(self, start, stop, freq, amp):
        self.freq = parseFreq(freq)
        self.start = start
        self.stop = stop
        self.amp = amp
        
    @abstractmethod
    def create_ampArr(self, start, stop):
        print("not implemented")
    
    @abstractmethod        
    def create_freqArr(self, start, stop):
        print("not implemented")
    
    #This method can be overloaded as well in special instruments.
    def toArray(self, secPerBar):
        start = mTime_to_aTime(self.start, secPerBar)
        stop = mTime_to_aTime(self.stop, secPerBar)
        arrLen = stop - start
        self.create_ampArr(start, stop)
        self.create_freqArr(start, stop)
        phase = 0
        data = np.zeros(arrLen)
        for i in range(len(data)):
            data[i] = self.ampArr[i] * self.waveForm[np.int64(phase)]
            phase += 1024 * self.freqArr[i] / 44100        #1024 is the length of the waveform array
            while (phase >= 1024):
                phase -= 1024
        return (data, start, stop)