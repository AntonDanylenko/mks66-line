from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    if(y1-y0<=x1-x0 and y1-y0>=0): #250 250 500 400
        d = y1+y1-y0-y0+x0-x1
        while x<=x1:
            plot(screen, color, x, y)
            if d>0:
                y+=1
                d+=x0+x0-x1-x1
            x+=1
            d+=y1+y1-y0-y0
    elif (y1-y0>x1-x0 and x1-x0>=0): #250 250 400 500
        d = y1-y0+x0+x0-x1-x1
        while y<=y1:
            plot(screen, color, x, y)
            if d<0:
                x+=1
                d+=y1+y1-y0-y0
            y+=1
            d+=x0+x0-x1-x1
    elif (y1-y0>=x0-x1): #250 250 500 100
        d = y1+y1-y0-y0+x0-x1
        while x<=x1:
            plot(screen, color, x, y)
            if d>0:
                y-=1
                d+=x0+x0-x1-x1
            x+=1
            d+=y1+y1-y0-y0
    elif (y1-y0<x0-x1): #250 250 400 0
        d = y1-y0+x0+x0-x1-x1
        while y>=y1:
            plot(screen, color, x, y)
            if d<0:
                x+=1
                d+=y1+y1-y0-y0
            y-=1
            d+=x0+x0-x1-x1
