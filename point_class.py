#!/usr/bin/env python

'''
Consider this code snippet
    """
    p1 = Point(x=12, y=4)
    p2 = Point(x=3, y=32)
    print (p1.distance_to(p2))
    """

Write a Python script and a "Point" class that makes the above code work.
'''

import numpy as np

class Point():
    def __init__(self,x,y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        self._x = new_x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        self._y = new_y

    def distance_to(self,point):
        return np.sqrt((self._x - point.x)**2 + (self._y - point.y)**2)

p1 = Point(x=12,y=4)
p2 = Point(x=3,y=32)

print(p1.distance_to(p2))
