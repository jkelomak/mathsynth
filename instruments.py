#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 10:38:03 2018

@author: stobe
"""

#----Module description----

#This module is where one adds new custom instruments to his composition. 
#It features amplitude changing in time, frequency changing in time as well as 
#custom waveforms. One may also use the overtones to waveform function to simply
#enter the involved overtones as an array. These instruments are examples,
#nothing more.

#ADVICE:
#Overtones above 22kHz cause aliasing so they should be avoided. For the middle
#A at 440 hz that means 50 overtones

#Amplitude array values should be somewhat continuous, otherwise there will be
#clicks.


import sound as snd
import numpy as np

#----Utility functions----

def OTtoWaveform(OTArr):
    tbl = np.zeros(1024)
    for i in range(1024):
        for j in range(len(OTArr)):
            tbl[i] += OTArr[j] * np.sin( 2 * np.pi * i / 1024) * (j + 1)
    return tbl

#----Instruments----
    

class testInst(snd.Snd):
    
    def __init__(self, start, stop, freq, amp):
        super().__init__(start, stop, freq, amp)
        self.waveForm = OTtoWaveform([1])
        
    def create_ampArr(self, start, stop):
        ampArr = np.zeros(stop - start)
        ampArr.fill(self.amp)
        self.ampArr = ampArr 
        
    def create_freqArr(self, start, stop):
        freqArr = np.zeros(stop - start)
        freqArr.fill(self.freq)
        self.freqArr = freqArr
        
class light(snd.Snd):
    
    def __init__(self, start, stop, freq, amp):
        super().__init__(start, stop, freq, amp)
        self.waveForm = OTtoWaveform([1, 1, 0.3, 0.6, 0.2, 0.1, 0.1, 0.3])
    
    #inefficient calculations, should be using fill and concatenate
    def create_ampArr(self, start, stop):
        ampArr = np.zeros(stop - start)
        i = 0
        amp = self.amp
        while (i < 50):
            ampArr[i] = i*(amp/50)
            i += 1
        while (i < stop - start - 100) and (i < 4000):
            ampArr[i] = amp
            i += 1
        for i in range(4000, stop - start - 100):
            if (i%100) == 0:
                amp *= 0.99
            ampArr[i] = amp
        for i in range(stop- start -100, stop - start):
            amp *= 0.93
            ampArr[i] = amp
        self.ampArr = ampArr 
        
    def create_freqArr(self, start, stop):
        freqArr = np.zeros(stop - start)
        freqArr.fill(self.freq)
        self.freqArr = freqArr
        
class light2(snd.Snd):
    
    def __init__(self, start, stop, freq, amp):
        super().__init__(start, stop, freq, amp)
        self.waveForm = OTtoWaveform([1, 0.8, 0.3, 0.6, 0.2, 0.1, 0.1, 0.3])
    
    #inefficient calculations, should be using fill and concatenate
    def create_ampArr(self, start, stop):
        ampArr = np.zeros(stop - start)
        i = 0
        amp = self.amp
        while (i < 50):
            ampArr[i] = i*(amp/50)
            i += 1
        while (i < stop - start - 100) and (i < 6000):
            ampArr[i] = amp
            i += 1
        while (i < 12000) and (i < stop - start - 100):
            if (i%12) == 0:
                amp = 0.2 * self.amp + (amp - 0.2 * self.amp) * 0.99
            ampArr[i] = amp
            i += 1
        while (i < stop - start - 100):
            if (i%100) == 0:
                amp *= 0.99
            ampArr[i] = amp
            i += 1
        fade = amp
        for i in range(stop- start -100, stop - start - 10):
            amp -= fade/90
            ampArr[i] = amp
        self.ampArr = ampArr 
        
    def create_freqArr(self, start, stop):
        freqArr = np.zeros(stop - start)
        freqArr.fill(self.freq)
        self.freqArr = freqArr
        
class light3(snd.Snd):
    
    def __init__(self, start, stop, freq, amp):
        super().__init__(start, stop, freq, amp)
        self.waveForm = OTtoWaveform([1, 0.8, 0.3, 0.6, 0.2, 0.1, 0.1, 0.3, 0, 0, 0, 0.1, 0, 0, 0, 0.05])
    
    #inefficient calculations, should be using fill and concatenate
    def create_ampArr(self, start, stop):
        ampArr = np.zeros(stop - start)
        i = 0
        amp = self.amp
        while (i < 50):
            ampArr[i] = i*(amp/50)
            i += 1
        while (i < stop - start - 100) and (i < 4000):
            ampArr[i] = amp
            i += 1
        while (i < 12000) and (i < stop - start - 100):
            if (i%12) == 0:
                amp = 0.1 * self.amp + (amp - 0.1 * self.amp) * 0.99
            ampArr[i] = amp
            i += 1
        while (i < stop - start - 100):
            if (i%100) == 0:
                amp *= 0.99
            ampArr[i] = amp
            i += 1
        fade = amp
        for i in range(stop- start -100, stop - start - 10):
            amp -= fade/90
            ampArr[i] = amp
        self.ampArr = ampArr 
        
    def create_freqArr(self, start, stop):
        freqArr = np.zeros(stop - start)
        freqArr.fill(self.freq)
        self.freqArr = freqArr

class faggot(snd.Snd):
    
    def __init__(self, start, stop, freq, amp):
        super().__init__(start, stop, freq, amp)
        OTarr = []
        for i in range(20):
            OTarr.append(2**(-i/2))
        self.waveForm = OTtoWaveform(OTarr)
    
    def create_ampArr(self, start, stop):
        ampArr = np.zeros(stop - start)
        i = 0
        amp = self.amp*0.8
        while (i < 200):
            ampArr[i] = i*(amp/200)
            i += 1
        while (i < stop - start -100) and (i < 4000):
            ampArr[i] = amp
            i += 1
        for i in range(4000, stop - start -100):
            if (i%500) == 0:
                amp *= 0.99
            ampArr[i] = amp
        fade = amp
        for i in range(stop- start -100, stop - start - 10):
            amp -= fade/90
            ampArr[i] = amp
        self.ampArr = ampArr 
        
    def create_freqArr(self, start, stop):
        freqArr = np.zeros(stop - start)
        for i in range(len(freqArr)):
            freqArr[i] = self.freq* 1.0003**(np.sin( 6 * np.pi* i / 44100))
        self.freqArr = freqArr
        
