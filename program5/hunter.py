# A Hunter is both a Mobile_Simulton and a Pulsator: it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2



class Hunter(Pulsator,Mobile_Simulton):
    def __init__(self,x,y,angle):
        self._x       = x
        self._y       = y
        self._speed   = 5
        self._width = 20
        self._height = 20
        self._angle   = angle
        self._color   = "black"
        self.radius = 10
        self.simus = set()
        
    def update(self):
        self.move()
        self.wall_bounce()
