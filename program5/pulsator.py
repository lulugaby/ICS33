# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole
import math

class Pulsator(Black_Hole): 
    radius = 10 
    def __init__(self,x,y): 
        self.time     =0 
        self._x       = x
        self._y       = y
        self._speed   = 0
        self._angle   = 0
        self._color   = 'black'
    
    

    def eat(self,l):
        self.time = 0 
        Pulsator.radius += len(l)
    
    def update(self,model):
        self.move()
        self.wall_bounce(model)

    
    def  move(self):
        #print(Pulsator.radius, self.time)
        self.time +=1
        if Pulsator.radius==0 : self.color = 'white'
        if self.time %30 == 0 and Pulsator.radius!=0:
            Pulsator.radius-=1
        self._x += self._speed*math.cos(self._angle)
        self._y += self._speed*math.sin(self._angle)
 
                
    def bounce(self,barrier_angle):
        self._angle = 2*barrier_angle - self._angle

        
    def wall_bounce(self,model):
        mw,mh    = model.world()
        
        left_x   = self._x - Pulsator.radius
        right_x  = self._x + Pulsator.radius
        top_y    = self._y - Pulsator.radius
        bottom_y = self._y + Pulsator.radius

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
        #print(Pulsator.radius)
        canvas.create_oval(self._x-Pulsator.radius      , self._y-Pulsator.radius,
                                    self._x+Pulsator.radius, self._y+Pulsator.radius,
                                    fill=self._color)
