# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 14:08:54 2018

@author: Jouko
"""

#This is an example of using the codebase. Running the code produces the
#wav file with the track.

import track
import instruments as i

t = track.Track(3, 10)


#---Bells---

for j in {0, 1, 3, 4, 6, 7}:
    amp = 0.1
    t.add(i.light(0 + j, 0.5 + j, "C5", amp))
    t.add(i.light(1/8 + j, 1/8 + 0.5 + j, "E5", amp))
    t.add(i.light(2/8 + j, 2/8 + 0.5 + j, "G5", amp))
    t.add(i.light(3/8 + j, 3/8 + 0.5 + j, "C6", amp))
    t.add(i.light(4/8 + j, 4/8 + 0.5 + j, "D6", amp))
    t.add(i.light(5/8 + j, 5/8 + 0.5 + j, "C6", amp))
    t.add(i.light(6/8 + j, 6/8 + 0.5 + j, "G5", amp))
    t.add(i.light(7/8 + j, 7/8 + 0.5 + j, "E5", amp))

for j in {2, 5}:
    amp = 0.1
    t.add(i.light(0 + j, 0.5 + j, "B-4", amp))
    t.add(i.light(1/8 + j, 1/8 + 0.5 + j, "D5", amp))
    t.add(i.light(2/8 + j, 2/8 + 0.5 + j, "F5", amp))
    t.add(i.light(3/8 + j, 3/8 + 0.5 + j, "B-5", amp))
    t.add(i.light(4/8 + j, 4/8 + 0.5 + j, "C6", amp))
    t.add(i.light(5/8 + j, 5/8 + 0.5 + j, "B-5", amp))
    t.add(i.light(6/8 + j, 6/8 + 0.5 + j, "A-5", amp))
    t.add(i.light(7/8 + j, 7/8 + 0.5 + j, "E5", amp))

#---Faggot---

t.add(i.faggot(0, 14/16, "B3", 0.1))
t.add(i.faggot(14/16, 15/16, "A3", 0.1))
t.add(i.faggot(15/16, 16/16, "B3", 0.1))

t.add(i.faggot(1, 17/16, "F+3", 0.1))
t.add(i.faggot(17/16, 2, "E3", 0.1))

t.add(i.faggot(2, 2 +1/8, "E3", 0.1))
t.add(i.faggot(2 + 1/8, 2 +2/8, "F3", 0.1))
t.add(i.faggot(2 + 2/8, 2 +3/8, "E3", 0.1))
t.add(i.faggot(2 + 3/8, 2 +6/8, "A-3", 0.1))
t.add(i.faggot(2 + 6/8, 2 +7/8, "B-3", 0.1))
t.add(i.faggot(2 + 7/8, 3, "C4", 0.1))

t.add(i.faggot(3, 3 + 1/8, "C3", 0.1))
t.add(i.faggot(3 + 1/8, 3 + 4/8, "A-3", 0.1))
t.add(i.faggot(3 + 4/8, 3 + 6/8, "B-3", 0.1))
t.add(i.faggot(3 + 6/8, 3 + 8/8, "A-3", 0.1))

t.add(i.faggot(4, 4 + 1/16, "G3", 0.1))
t.add(i.faggot(4 + 1/16, 4 + 2/16, "E3", 0.1))
t.add(i.faggot(4 + 2/16, 5, "A-2", 0.1))

t.add(i.faggot(5, 5.5, "G2", 0.1))
t.add(i.faggot(5.5, 5.75, "A-3", 0.1))
t.add(i.faggot(5.75, 6, "G3", 0.1))
t.add(i.faggot(6, 7, "G3", 0.1))

#---Bass---

t.add(i.testInst(0, 2, "C2", 0.05))
t.add(i.testInst(2, 3, "B-1", 0.05))
t.add(i.testInst(3, 5, "C2", 0.05))
t.add(i.testInst(5, 6, "B-1", 0.05))
t.add(i.testInst(6, 8, "C2", 0.05))

t.add(i.testInst(0, 2, "C8", 0.002))
t.add(i.testInst(2, 3, "B-7", 0.002))
t.add(i.testInst(3, 5, "C8", 0.002))
t.add(i.testInst(5, 6, "B-7", 0.002))
t.add(i.testInst(6, 8, "C8", 0.002))


t.compileTrack("test.wav")
print("done")




