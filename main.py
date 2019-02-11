from display import *
from draw import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
color1 = [ 255, 0, 0 ]
color2 = [ 0, 0, 255 ]
color3 = [ 255, 255, 255 ]

'''#oct 1
draw_line(250,250,300,499,screen,color)
plot(screen,color1,300,499)
#oct 2
draw_line(250,250,499,400,screen,color)
plot(screen,color1,499,400)
draw_line(250,250,250,400,screen,color)
plot(screen,color1,250,400)
draw_line(250,250,499,250,screen,color)
plot(screen,color1,499,250)

#oct 8
draw_line(250,250,499,100,screen,color2)
plot(screen,color1,499,100)
draw_line(0,2,2,1,screen,color2)
plot(screen,color1,2,1)
#oct 7
draw_line(250,250,400,5,screen,color2)
plot(screen,color1,400,5)
draw_line(0,2,1,0,screen,color2)
#plot(screen,color1,1,0)
draw_line(250,250,250,5,screen,color2)
plot(screen,color1,250,5)

draw_line(250,250,100,499,screen,color3)
plot(screen,color1,100,499)
draw_line(250,250,100,120,screen,color3)
plot(screen,color1,100,120)
draw_line(250,250,100,300,screen,color3)
plot(screen,color1,100,300)
draw_line(250,250,100,50,screen,color3)
plot(screen,color1,100,50)
'''

x = -200
#y1 = -200
while x <= 200:
    y = int(math.floor(math.sqrt(40000 - (x * x))))
    #x1 = int(math.floor(math.sqrt(40000 - (y1 * y1))))
    #draw_line(250, 250, x+250, y+250, screen, [(255+screen[500-1-y-250][x+250][0])/2,                                (85+screen[500-1-y-250][x+250][1])/2,                                    (int(math.floor(((x+200)*255)/401))+screen[500-1-y-250][x+250][2])/2])
    #draw_line(250, 250, x+250, 250-y, screen, [(255+screen[500-1-y-250][x+250][0])/2,                                (85+screen[500-1-y-250][x+250][1])/2,                                    (int(math.floor(((x+200)*255)/401))+screen[500-1-y-250][x+250][2])/2])
    #draw_line(250, 250, x+250, 250-y, screen, [(int(math.floor(((x+200)*255)/401))+screen[500-1+y-250][x+250][0])/2, (85+screen[500-1+y-250][x+250][1])/2,                                    (255+screen[500-1+y-250][x+250][2])/2])
    #draw_line(250, 250, x1+250, y1+250, screen, [(85+screen[500-1-y1-250][x1+250][0])/2,                             (255+screen[500-1-y1-250][x1+250][1])/2,                                 (int(math.floor(((y1+200)*255)/401))+screen[500-1-y1-250][x1+250][2])/2])
    #draw_line(250, 250, 250-x1, y1+250, screen, [(85+screen[500-1-y1-250][x1+250][0])/2,                             (255+screen[500-1-y1-250][x1+250][1])/2,                                 (int(math.floor(((y1+200)*255)/401))+screen[500-1-y1-250][x1+250][2])/2])
    #draw_line(250, 250, 250-x1, y1+250, screen, [(85+screen[500-1-y1-250][250-x1][0])/2,                             (int(math.floor(((y1+200)*255)/401))+screen[500-1-y1-250][250-x1][1])/2, (255+screen[500-1-y1-250][250-x1][2])/2])
    draw_line(250, 250, x+250, y+250, screen, color)
    draw_line(250, 250, x+250, 250-y, screen, color)
    x+=1
    #y1+=1

y = -100
while y <= 100:
    x = int(math.floor(math.sqrt(10000 - (y * y))))
    draw_line(250, 250, x+250, y+250, screen, color1)
    draw_line(250, 250, 250-x, y+250, screen, color1)
    y+=1

display(screen)
save_extension(screen, 'img.png')
