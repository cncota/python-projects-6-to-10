import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter


import math,random


running     = False
cycle_count = 0
balls       = set()
object = None
simu = set()

def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

def random_angle():
    # between 0 and 2pi
    return random.random()*math.pi*2


def reset ():
    global running,cycle_count,balls
    running     = False
    cycle_count = 0
    balls       = set()


def start():
    global running
    running = True


def stop():
    global running
    running = False


def step ():
    global cycle_count
    global running
    if running == True:
        for i in [1]:
            cycle_count += 1
            for b in balls:
                b.update()
            running = False 
            break
    elif running == False:
        for i in [1]:
            cycle_count += 1
            for b in balls:
                b.update()
            break
        


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global object
    object = str(kind)


def mouse_click(x,y):
    global object
    if object == 'Ball':
        balls.add( Ball(x,y,random_angle()))
    elif object == "Floater":
        balls.add(Floater(x,y,random_angle()))
    elif object == "Black_Hole":
        simu.add(Black_Hole(x,y))
    elif object == "Pulsator":
        simu.add(Pulsator(x,y))
    elif object == "Remove":
        g = balls
        h = set()
        k = set()
        for f in g:
            if f.contains((x,y)):
                h.add(f)
        for s in simu:
            if s.contains((x,y)):
                k.add(s)
        for l in h:
            remove(l)
        for b in k:
            simu.remove(b)
        pass
    elif object == "Hunter":
        simu.add(Hunter(x,y, random_angle()))

#add simulton s to the simulation
def add(s):
    balls.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    balls.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    g = balls
    h = set()
    for i in g:
        if p.contains((i._x,i._y)):
            h.add(i)
    for l in h:
        remove(l)
    display_all()
                


#call update for every simulton in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        for b in balls:
            b.update()
        for s in simu:
            find(s)
            s.update()


#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    # Easier to delete all and display all; could use move with more thought
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in balls:
        b.display(controller.the_canvas)
    
    for s in simu:
        s.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(balls))+" balls/"+str(cycle_count)+" cycles")
