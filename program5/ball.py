# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).


from prey import Prey


class Ball(Prey):
    radius = 5
    
    def __init__(self,x,y,angle):
        self._x       = x
        self._y       = y
        self._speed   = 5
        self._width = 10
        self._height = 10
        self._angle   = angle
        self._color   = "blue"
        
    def update(self):
        self.move()
        self.wall_bounce()
        
    def display(self,canvas):
        canvas.create_oval(self._x-Ball.radius      , self._y-Ball.radius,
                                self._x+Ball.radius, self._y+Ball.radius,
                                fill=self._color)
        
    def contains(self,xy):
        if ((self._x -xy[0])**2  + (self._y -xy[1])**2)**.5 < self.radius:
            return True
        else:
            return False