# The Hunter class is derived from Pulsator first and then Mobile_Simulton.
#   It inherits updating/displaying from Pusator and Mobile_Simulton: it pursues
#   close prey, or moves in a straight line, like its Mobile_Simultion base.


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import math



class Hunter(Pulsator, Mobile_Simulton):  
    radius = 5 
    def __init__(self,x,y): 
        self._x       = x
        self._y       = y
        self._speed   = 5
        self._angle   = 0
        self._color   = 'green'
        self.time=0

    def balls(self, balls):
        self._balls = balls
    
    def eat(self,l):
        self.time = 0 
        Hunter.radius += len(l)

    def hunting(self):
        if self._balls != None:
            for b in self._balls:
                if 'Black' not in str(b) and "Pulsator" not in str(b) and "Hunter" not in str(b):
                    for i in range(200):
                        x  = [x for x in range(int(self._x-i), int(self._x + i))]
                        y = [x for x in range(int(self._y-i), int(self._y + i))]
                        if b._x in x and b._y in y:
                            #print('angle')
                            self._angle = math.atan2(b._y-self._y, b._x-self._x)
      
        
    
    def update(self,model):
        self.hunting()
        self.move()
        self.wall_bounce(model)

    
    def  move(self):
        self.time +=1
        if Hunter.radius==0 : self.color = 'white'
        if self.time %30 == 0 and Hunter.radius!=0:
            Hunter.radius-=1
        self._x += self._speed*math.cos(self._angle)
        self._y += self._speed*math.sin(self._angle)
 
                
    def bounce(self,barrier_angle):
        self._angle = 2*barrier_angle - self._angle

        
    def wall_bounce(self,model):
        mw,mh    = model.world()
        
        left_x   = self._x - Hunter.radius
        right_x  = self._x + Hunter.radius
        top_y    = self._y - Hunter.radius
        bottom_y = self._y + Hunter.radius

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
       if Pulsator.radius != 0:
        canvas.create_oval(self._x-Hunter.radius      , self._y-Hunter.radius,
                                    self._x+Hunter.radius, self._y+Hunter.radius,
                                    fill=self._color)

