# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 

import math
from prey import Prey
import random


class Ball(Prey): 
    radius = 5

    def __init__(self,x,y): 
        self._x       = x
        self._y       = y
        self._speed   = 5
        self._angle   = random.randrange(0,360)
        self._color   = 'blue'
    
    def update(self,model):
        self.move()
        self.wall_bounce(model)

    
    def  move(self):
        self._x += self._speed*math.cos(self._angle)
        self._y += self._speed*math.sin(self._angle)
 
                
    def bounce(self,barrier_angle):
        self._angle = 2*barrier_angle - self._angle

        
    def wall_bounce(self,model):
        mw,mh    = model.world()
        
        left_x   = self._x - Ball.radius
        right_x  = self._x + Ball.radius
        top_y    = self._y - Ball.radius
        bottom_y = self._y + Ball.radius

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
       canvas.create_oval(self._x-Ball.radius      , self._y-Ball.radius,
                                self._x+Ball.radius, self._y+Ball.radius,
                                fill=self._color)

