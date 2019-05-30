# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey

class Black_Hole(Simulton):
    radius = 10
    
    def __init__(self,x,y):
        self._x       = x
        self._y       = y
        self._width = 20
        self._height = 20
        self._color   = "black"
        self.simus = set()
        self.radius = 10
        
    def update(self):
        return self.simus
        
    def display(self,canvas):
        canvas.create_oval(self._x-Black_Hole.radius      , self._y-Black_Hole.radius,
                                self._x+Black_Hole.radius, self._y+Black_Hole.radius,
                                fill=self._color)
       
    def contains(self,xy):
        if ((self._x -xy[0])**2  + (self._y -xy[1])**2)**.5 < self.radius:
            self.simus.add(xy)
            return True
        else:
            return False