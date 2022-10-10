import controller
import model   # Calling update in update_all passes a reference to this model
import math
import random
#Use the reference to this module to pass it to update methods

from ball      import Ball
from blackhole import Black_Hole
from floater   import Floater
from hunter    import Hunter
from pulsator  import Pulsator
from special import CATS


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running     = False
last_cycle = 0 
cycle_count = 0
balls       = set()
click = (None,None)
_step = False
_ball = False
_remove = False
_black = False
_pulsator = False
_float  = False
_hunter = False
Bholes = set()

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,balls
    running     = False
    cycle_count = 0
    balls       = set()


#start running the simulation
def start ():
    global running
    global _step
    running = True
    _step = False
    #b_hole()
    


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False
    
    


#step just one update in the simulation
def step():
    global _step
    global running
    running = True
    _step = True
   
    
    


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global _ball
    global _remove
    global _black
    global _pulsator
    global _float
    global _hunter
    #global balls
    _ball = False
    _remove = False
    _black = False
    _pulsator = False
    _float  = False
    _hunter = False
    print('select onject', kind)
    if kind == 'Ball':
        _ball = True
    if kind == 'Remove':
        _remove = True 
    if kind == 'Black_Hole':
        _black = True
    if kind == 'Pulsator':
        _pulsator = True
    if kind == 'Floater':
        _float = True
    if kind == "Hunter":
        _hunter = True 
    if kind == "Special":
        add(CATS())

    


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global click
    global _ball
    global Bholes
    #global _pulsator
    #global _float
    click = (x,y)
    if _ball == True:
        add(Ball(click[0],click[1]))
    if _float == True:
        add(Floater(click[0],click[1]))
    if _remove == True:
        remove(click)
    if _black == True:
        add(Black_Hole(click[0],click[1]))
        Bholes.add(Black_Hole(click[0],click[1]))
    if _pulsator == True:
        add(Pulsator(click[0],click[1]))
        Bholes.add(Pulsator(click[0],click[1]))
    if _hunter == True :
        add(Hunter(click[0],click[1]))
        Bholes.add(Hunter(click[0],click[1]))
    #print(click)
    
#def cats():
 #   add(CATS())


#add simulton s to the simulation
def add(s):
    global balls
    #print('add', s)
    balls.add(s)
    pass
    

# remove simulton s from the simulation    
def remove(s):
    global balls
    b = find(s)
    if b != None:
        balls.remove(b)
    #print(b)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    global balls
    for b in balls:
        x = [i for i in range(int(b._x-b.radius), int(b._x+b.radius))]
        y = [i for i in range(int(b._y-b.radius), int(b._y+b.radius))]
        if p[0] in x and p[1] in y:
            return b

def b_hole():
    global balls
    global Bholes
    Bholes = set()

    for b in balls:
        if 'Black'  in str(b) or "Pulsator"  in str(b) or "Hunter"  in str(b):
            Bholes.add(b)

    if Bholes!=set() and balls != set():
        for h in Bholes:
            left_right = [i for i in range(int(h._x-h.radius), int(h._x+h.radius))]
            top_bottom = [i for i in range(int(h._y-h.radius), int(h._y+h.radius))]
            _remove =  set()
            for b in balls:
                if 'Black' not in str(b) and "Pulsator" not in str(b) and "Hunter" not in str(b):
                    ball_left_right = [i for i in range(int(b._x-b.radius), int(b._x+b.radius))]
                    ball_top_bottom = [i for i in range(int(b._y-b.radius), int(b._y+b.radius))]

                    if len(left_right + ball_left_right) != len(set(left_right + ball_left_right)) and len(top_bottom + ball_top_bottom)!= len(set(top_bottom + ball_top_bottom)):
                        _remove.add(b)
            
            for x in _remove:
                print('remove', remove)
                balls.remove(x)
            if len(_remove)>0:
                if "Pulsator" in str(h) or "Hunter" in str(h):
                    h.eat(_remove)

def hunt():
    global balls
    for k in balls:
        if 'Hunter' in str(k):
            k.balls(balls)
           
                        
            





#For each simulton in model's simulation, call update on it, passing along model
#This function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton's update do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global running
    global _step
    global last_cycle
    global cycle_count
    global balls
    
    hunt()
    b_hole()
    balls = {b for b in balls if b.radius!=0}
    if running:
        cycle_count += 1
        if _step==True and last_cycle<cycle_count: running=False
        last_cycle = cycle_count
        for b in balls:
            b.update(model)

#Animation: (a) delete all simultons on the canvas; (b) call display on all
#  simultons being simulated, adding back each to the canvas, often in a new
#  location; (c) update the label defined in the controller showing progress 
#This function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    # Easier to delete all and display all; could use move with more thought
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in balls:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(balls))+" balls/"+str(cycle_count)+" cycles")
