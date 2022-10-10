# This Black_Hole class is derived from Simulton; for updating it finds+removes
#   objects (of any class Prey derived class) whose center is contained inside
#   its radius (returning a set of all eaten simultons), and it displays as a
#   black circle with a radius of 10 (width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter
import math
from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):  
    radius = 10

    def __init__(self,x,y): 
        self._x       = x
        self._y       = y
        self._speed   = 0
        self._angle   = 0
        self._color   = 'black'
    
    def update(self,model):
        self.move()
        self.wall_bounce(model)

    
    def move(self):
        self._x += self._speed*math.cos(self._angle)
        self._y += self._speed*math.sin(self._angle)
 
                
    def bounce(self,barrier_angle):
        self._angle = 2*barrier_angle - self._angle

        
    def wall_bounce(self,model):
        mw,mh    = model.world()
        
        left_x   = self._x - Black_Hole.radius
        right_x  = self._x + Black_Hole.radius
        top_y    = self._y - Black_Hole.radius
        bottom_y = self._y + Black_Hole.radius

        if left_x < 0:
            self.bounce(math.pi/2)
            self._x += -2*left_x
        elif right_x > mw:
            self.bounce(math.pi/2);
            self._x += 2*(mw-right_x)

        if top_y < 0:
            self.bounce(0);
            self._y += -2*top_y
        elif bottom_y > mh:
            self.bounce(0);
            self._y += 2*(mh-bottom_y) 
            
            
    def reverse(self):
        self._angle += math.pi

         
    def display(self,canvas):
       canvas.create_oval(self._x-Black_Hole.radius      , self._y-Black_Hole.radius,
                                self._x+Black_Hole.radius, self._y+Black_Hole.radius,
                                fill=self._color)
