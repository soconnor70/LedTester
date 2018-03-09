#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `assignment3_17205711` package."""


import unittest
from click.testing import CliRunner


from assignment3_17205711 import cli


class TestAssignment3_17205711(unittest.TestCase):
    """Tests for `assignment3_17205711` package."""

 def countLights(N, a2d):
    count = 0
    for i in range(N):
        for j in range(N):
            if a2d[i][j] == 1:
                count += 1
    return count


def turnOn(x1, x2, y1, y2, a2d):
    for i in range(int(x1), int(y1)+1):
        for j in range(int(x2), int(y2)+1):
            a2d[i][j] = 1
    return


def turnOff(x1, x2, y1, y2, a2d):
    for i in range(int(x1), int(y1)+1):
        for j in range(int(x2), int(y2)+1):
            a2d[i][j] = 0

    return



def switch(x1, x2, y1, y2, a2d):
    for i in range(int(x1), int(y1) +1):
        for j in range(int(x2), int(y2) +1):
            a2d[i][j] = 1 - a2d[i][j]

    return
    
N = 10
a2d = [ [0]*N for _ in range(N) ]
#a2d = []
#for x in range(10):
    #a2d.append([])
    #for y in range(10):
        #a2d[x].append(0)
        
#turnOn(0, 0, 2, 2, a2d)
turnOn(2, 2, 9, 9, a2d)
turnOff(3, 3, 4, 4, a2d)
switch(0, 0, 2, 2, a2d)
#print(a2d)
for a in a2d:
    print(a)

#print(a2d)
count = countLights(N, a2d)
print (count)