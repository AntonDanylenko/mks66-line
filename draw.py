from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    if(x1-x0>=0):
        if(y1-y0<=x1-x0 and y1-y0>=0): #0 2 2 3
            d = y1+y1-y0-y0+x0-x1 #0
            while x<=x1:
                plot(screen, color, x, y)
                if d>0:
                    y+=1
                    d+=x0+x0-x1-x1 #-4
                x+=1
                d+=y1+y1-y0-y0 #+2
        elif (y1-y0>x1-x0): #0 2 1 4
            d = y1-y0+x0+x0-x1-x1 #0
            while y<=y1:
                plot(screen, color, x, y)
                if d<0:
                    x+=1
                    d+=y1+y1-y0-y0 #+4
                y+=1
                d+=x0+x0-x1-x1 #-2
        elif (y1-y0>=x0-x1): #0 2 2 1
            d = 0-(y1+y1-y0-y0+x0-x1) #4
            while x<=x1:
                plot(screen, color, x, y)
                if d>0:
                    y-=1
                    d+=x0+x0-x1-x1 #-4
                x+=1
                d+=y0+y0-y1-y1 #+2
        elif (y1-y0<x0-x1): #0 2 1 0
            d = 0-(y1-y0+x0+x0-x1-x1) #-4
            while y>=y1:
                plot(screen, color, x, y)
                if d<0:
                    x+=1
                    d+=y0+y0-y1-y1 #+4
                y-=1
                d+=x0+x0-x1-x1 #-2
    else:
        draw_line(x1, y1, x0, y0, screen, color) #2 2 0 1
