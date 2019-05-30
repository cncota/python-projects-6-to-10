# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole):
    def __init__(self,x,y):
        self._x       = x
        self._y       = y
        self._width = 20
        self._height = 20
        self._color   = "black"
        self.simus = set()
        self.radius = 10
        self.counter = 0
        
        
    def update(self):
        self.counter += 1
        for x in self.simus:
            self._width += 1
            self._height += 1
            self.radius += 1
            self.counter = 0
        if self.counter > 30 and len(self.simus) == 0:
            self._width -= 1
            self._height -= 1
            self.radius -= 1
        return self.simus
            