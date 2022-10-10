# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random
import math 
import random

class Floater(Prey): 
    radius = 5
    def __init__(self,x,y): 
        self._x       = x
        self._y       = y
        self._speed   = 5
        self._angle   = random.randrange(0,360)
        self._color   = 'red'
        
    
    def update(self,model):
        self.move()
        self.wall_bounce(model)

    def  move(self):
        n = random.randrange(0,100)
        if n <=30:
            self._speed += random.uniform(-.5, .5)
            self._angle  = random.randrange(-28,28)
        
        self._x += self._speed*math.cos(self._angle)
        #if self._speed*math.sin(self._angle) in range(-3,7):
        self._y += self._speed*math.sin(self._angle)
        
        
           
    def bounce(self,barrier_angle):
        self._angle = 2*barrier_angle - self._angle
      
    def wall_bounce(self,model):
        mw,mh    = model.world()
        
        left_x   = self._x - Floater.radius
        right_x  = self._x + Floater.radius
        top_y    = self._y - Floater.radius
        bottom_y = self._y + Floater.radius

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
       canvas.create_oval(self._x-Floater.radius      , self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill=self._color)

