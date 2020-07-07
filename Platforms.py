from graphics import *
import random

def main():
    win = GraphWin("ksdhjf",500,500)
    win.setBackground("white")

    #tells how many lines to make
    lines = random.randint(3,10)
    #has the coords
    platformx = []
    platformy = []
    platformz = []
    

    #makes y coordinate then appends
    for i in range(1,lines):
        while True:
            y=random.randint(50,500)
            #Appends y if platformy is empty
            if len(platformy) == 0:
                platformy.append(y)
                continue
            #Calls function that checks if y coords are too close
            if validateY(y,platformy):
                platformy.append(y)
                break

    #makes x coord then appends
    for i in range(1,lines):
        while True:
            x=random.randint(0,500)
            #if list platformx is empty append x
            if len(platformx) == 0:
                platformx.append(x)
                continue
            #Calls function that makes sure that x coords don't overlap too much
            if validateX(x,platformx):
                platformx.append(x)
                break

    #makes second x cord then appends
    for i in range(1,lines):
        while True:
            z=random.randint(0,500)
            #if list platformz is empty append z (z still being an x coordinate)
            if len(platformz) == 0:
                platformz.append(z)
                continue
            #Cllas function that makes sure that the coords don't overlap too much
            if validateZ(z,platformz):
                platformz.append(z)
                break
        
    lineDistance(platformx,platformz)

    #Draws the line
    for i in range(0,len(platformy)):
        a=Point(platformx[i],platformy[i])
        b=Point(platformz[i],platformy[i])
        ln=Line(a,b)
        ln.setOutline(color_rgb(0,0,0))
        ln.setWidth(random.randint(1,5))
        ln.draw(win)

   
    #Closes the window
    win.getMouse()
    win.close()

def validateY(y,platformy):
    #Checks if the y coordinates are within 100 units (x is previous y coordinate 
    #and y is the current y coordinate being checked against the previous y coorinates)
    for x in platformy:
        if x<=y+50 and x>=y-50:
            return False
    return True

def validateX(x,platformx):
    #I split up the screen into 3 imaginary quadrants ((0,167),(168,334),(335,500)) and
    #made it so that if the previous x coordinate was in one quadrant, it would put 
    #the new x coordinate into one of the other 2 coordinates
    if platformx[-1]<167:
        if x<=167:
            return False
        if x>=168:
            return True
    if 167<=platformx[-1]<=334:
        if 167<=x<=334:
            return False   
        if x<167:
            return True
        if x>334:
            return True
    if 334<=platformx[-1]<=500:
        if 334<=x<=500:
            return False
        if x<334:
            return True

def validateZ(z,platformz):
    #Basically the exact same thing as validateX because to make sure that most of the 
    #platforms are not overlapping each other
    if platformz[-1]<167:
        if z<=167:
            return False
        if z>=168:
            return True
    if 167<=platformz[-1]<=334:
        if 167<=z<=334:
            return False   
        if z<167:
            return True
        if z>334:
            return True
    if 334<=platformz[-1]<=500:
        if 334<=z<=500:
            return False
        if z<334:
            return True

def lineDistance(platformx,platformz):
    for i in range(0,len(platformx)):
        if platformx[i]-platformz[i]<0:
            if platformz[i]-platformx[i]<50:
                x=platformx[i]-50
                platformx.pop(i)
                platformx.insert(i,x)
                break
        if platformx[i]-platformz[i]<50:
            x=platformz[i]-50
            platformx.pop(i)
            platformx.insert(i,x)

main()