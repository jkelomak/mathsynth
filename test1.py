#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 17:03:38 2018

@author: stobe
"""

#This is an example of using the codebase. Running the code produces the
#wav file with the track.

import track
import instruments as i

t = track.Track(3, 23)

#---Harmony---

harm = lambda start, stop, freq, amp: t.add(i.light3(start, stop, freq, amp))

bars = {0, 1, 4, 5}
for bar in bars:
    for j in range(8):
        amp = 0.2
        harm(j/8 + bar, (j+1)/8 + bar, "E5", amp)
        harm(j/8 + bar, (j+1)/8 + bar, "A5", amp)

bars = {2, 3, 6, 7}
for bar in bars:
    for j in range(8):
        amp = 0.2
        harm(j/8 + bar, (j+1)/8 + bar, "E-5", amp)
        harm(j/8 + bar, (j+1)/8 + bar, "A-5", amp)

bars = {8, 10, 12, 14}
for bar in bars:
    for j in range(8):
        amp = 0.2
        harm(j/8 + bar, (j+1)/8 + bar, "B4", amp)
        harm(j/8 + bar, (j+1)/8 + bar, "E5", amp)

bars = {9, 11, 13}
for bar in bars:
    for j in range(8):
        amp = 0.2
        harm(j/8 + bar, (j+1)/8 + bar, "C5", amp)
        harm(j/8 + bar, (j+1)/8 + bar, "F5", amp)
        
bars = {15}
for bar in bars:
    for j in range(8):
        amp = 0.2
        harm(j/8 + bar, (j+1)/8 + bar, "B-4", amp)
        harm(j/8 + bar, (j+1)/8 + bar, "E-5", amp)

bars = {16, 18}
for bar in bars:
    for j in range(4):
        amp = 0.2
        harm(j/8 + bar, (j+1)/8 + bar, "F4", amp)
        harm(j/8 + bar, (j+1)/8 + bar, "B-4", amp)

bars = {16.5, 18.5}
for bar in bars:
    for j in range(4):
        amp = 0.2
        harm(j/8 + bar, (j+1)/8 + bar, "F+4", amp)
        harm(j/8 + bar, (j+1)/8 + bar, "C5", amp)
        
bars = {17, 19}
for bar in bars:
    for j in range(4):
        amp = 0.2
        harm(j/8 + bar, (j+1)/8 + bar, "A-4", amp)
        harm(j/8 + bar, (j+1)/8 + bar, "E-5", amp)
        
bars = {17.5, 19.5}
for bar in bars:
    for j in range(4):
        amp = 0.2
        harm(j/8 + bar, (j+1)/8 + bar, "A-4", amp)
        harm(j/8 + bar, (j+1)/8 + bar, "D-5", amp)

bars = {20, 21}
for bar in bars:
    for j in range(8):
        amp = 0.2
        harm(j/8 + bar, (j+1)/8 + bar, "E5", amp)
        harm(j/8 + bar, (j+1)/8 + bar, "A5", amp)


#---Melody---    
        
mel = lambda start, stop, freq, amp: t.add(i.faggot(start, stop, freq, amp))

        
amp = 0.4
mel(0, 1/8, "A-4", amp)
mel(1/8, 2/8, "A4", amp)
mel(2/8, 3/8, "F4", amp)
mel(3/8, 4/8, "E4", amp)
mel(4/8, 1 + 3/8, "E-4", amp)
mel(1 + 3/8, 1 + 4/8, "A-4", amp)
mel(1 + 4/8, 1 + 5/8, "A4", amp)
mel(1 + 5/8, 1 + 6/8, "E4", amp)
mel(1 + 6/8, 1 + 7/8, "A4", amp)
mel(1 + 7/8, 1 + 8/8, "B4", amp)

mel(2, 2 +1/8, "B-4", amp)
mel(2 + 1/8, 2 + 2/8, "A-4", amp)
mel(2 + 2/8, 3, "E-4", amp)


mel(0 + 4, 1/8 + 4, "A-4", amp)
mel(1/8 + 4, 2/8 + 4, "A4", amp)
mel(2/8 + 4, 3/8 + 4, "F4", amp)
mel(3/8 + 4, 4/8 + 4, "E4", amp)
mel(4/8 + 4, 1 + 3/8 + 4, "E-4", amp)
mel(1 + 3/8 + 4, 1 + 4/8 + 4, "A-4", amp)
mel(1 + 4/8 + 4, 1 + 5/8 + 4, "A4", amp)
mel(1 + 5/8 + 4, 1 + 6/8 + 4, "E4", amp)
mel(1 + 6/8 + 4, 1 + 7/8 + 4, "A4", amp)
mel(1 + 7/8 + 4, 1 + 8/8 + 4, "B4", amp)

mel(2 + 4, 2 +1/8 + 4, "B-4", amp)
mel(2 + 1/8 + 4, 2 + 2/8 + 4, "A-4", amp)
mel(2 + 2/8 + 4, 3 + 4, "E-4", amp)

time = 8
mel(time, time + 1/8, "G+4", amp)
time += 1/8
mel(time, time + 1/8, "A+4", amp)
time += 1/8
mel(time, time + 1/8, "B4", amp)
time += 1/8
mel(time, time + 1/8, "A+4", amp)
time += 1/8
mel(time, time + 1/8, "G+4", amp)
time += 1/8
mel(time, time + 1/8, "F4", amp)
time += 1/8
mel(time, time + 1/8, "E4", amp)
time += 1/8
mel(time, time + 1/8, "F4", amp)
time += 1/8
mel(time, time + 1/8, "E4", amp)
time += 1/8
mel(time, time + 1/8, "F4", amp)
time += 1/8
mel(time, time + 1/8, "B4", amp)
time += 1/8
mel(time, time + 1/8, "A4", amp)
time += 1/8
mel(time, time + 4/8, "F4", amp)
time += 4/8

time = 10
mel(time, time + 1/8, "G+4", amp)
time += 1/8
mel(time, time + 1/8, "A+4", amp)
time += 1/8
mel(time, time + 1/8, "B4", amp)
time += 1/8
mel(time, time + 1/8, "A+4", amp)
time += 1/8
mel(time, time + 1/8, "G+4", amp)
time += 1/8
mel(time, time + 1/8, "F4", amp)
time += 1/8
mel(time, time + 1/8, "E4", amp)
time += 1/8
mel(time, time + 1/8, "F4", amp)
time += 1/8
mel(time, time + 1/8, "E4", amp)
time += 1/8
mel(time, time + 1/8, "F4", amp)
time += 1/8
mel(time, time + 1/8, "B4", amp)
time += 1/8
mel(time, time + 1/8, "A4", amp)
time += 1/8
mel(time, time + 4/8, "F4", amp)
time += 4/8

time = 12
mel(time, time + 1/8, "G+4", amp)
time += 1/8
mel(time, time + 1/8, "A+4", amp)
time += 1/8
mel(time, time + 1/8, "B4", amp)
time += 1/8
mel(time, time + 1/8, "A+4", amp)
time += 1/8
mel(time, time + 1/8, "G+4", amp)
time += 1/8
mel(time, time + 1/8, "F4", amp)
time += 1/8
mel(time, time + 1/8, "E4", amp)
time += 1/8
mel(time, time + 1/8, "F4", amp)
time += 1/8
mel(time, time + 1/8, "E4", amp)
time += 1/8
mel(time, time + 1/8, "F4", amp)
time += 1/8
mel(time, time + 1/8, "B4", amp)
time += 1/8
mel(time, time + 1/8, "G4", amp)
time += 1/8
mel(time, time + 4/8, "F4", amp)
time += 4/8

time = 14
mel(time, time + 1/8, "G+4", amp)
time += 1/8
mel(time, time + 1/8, "A+4", amp)
time += 1/8
mel(time, time + 1/8, "B4", amp)
time += 1/8
mel(time, time + 1/8, "A+4", amp)
time += 1/8
mel(time, time + 1/8, "G+4", amp)
time += 1/8
mel(time, time + 1/8, "F4", amp)
time += 1/8
mel(time, time + 1/8, "E4", amp)
time += 1/8
mel(time, time + 1/8, "F4", amp)
time += 1/8
mel(time, time + 1/8, "E-4", amp)
time += 1/8
mel(time, time + 1/8, "D4", amp)
time += 1/8
mel(time, time + 6/8, "B-3", amp)
time += 6/8

time = 16
mel(time, time + 1/8, "B3", amp)
time += 1/8
mel(time, time + 1/8, "B-3", amp)
time += 1/8
mel(time, time + 1/8, "D-4", amp)
time += 1/8
mel(time, time + 1/8, "D4", amp)
time += 1/8
mel(time, time + 1/8, "D+4", amp)
time += 1/8
mel(time, time + 1/8, "E4", amp)
time += 1/8
mel(time, time + 1/8, "F4", amp)
time += 1/8
mel(time, time + 1/8, "E4", amp)
time += 1/8
mel(time, time + 1/8, "B3", amp)
time += 1/8
mel(time, time + 1/8, "B-3", amp)
time += 1/8
mel(time, time + 6/8, "A-3", amp)
time += 6/8

time = 18
mel(time, time + 1/8, "B3", amp)
time += 1/8
mel(time, time + 1/8, "B-3", amp)
time += 1/8
mel(time, time + 1/8, "D-4", amp)
time += 1/8
mel(time, time + 1/8, "D4", amp)
time += 1/8
mel(time, time + 1/8, "D+4", amp)
time += 1/8
mel(time, time + 1/8, "E4", amp)
time += 1/8
mel(time, time + 1/8, "F4", amp)
time += 1/8
mel(time, time + 1/8, "E4", amp)
time += 1/8
mel(time, time + 1/8, "B3", amp)
time += 1/8
mel(time, time + 1/8, "B-3", amp)
time += 1/8
mel(time, time + 6/8, "A-3", amp)
time += 6/8

mel(20, 22, "A3", amp)

t.compileTrack("test1.wav")
print("done")