# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random
import math,random


def random_speed():
    # Magnitude is 5-10
    return random.randint(1,+5)

class Floater(Prey):
    radius = 5
    
    def __init__(self,x,y, angle):
        self._x       = x
        self._y       = y
        self._speed   = random_speed()
        self._width = 10
        self._height = 10
        self._angle   = angle
        self._color   = "red"
        
    def update(self):
        self.move()
        self.wall_bounce()
        
    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius      , self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill=self._color)
        
    def contains(self,xy):
        if ((self._x -xy[0])**2  + (self._y -xy[1])**2)**.5 < self.radius:
            return True
        else:
            return False