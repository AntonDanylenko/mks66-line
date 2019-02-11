from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
color1 = [ 255, 0, 0 ]
color2 = [ 0, 0, 255 ]
color3 = [ 127, 0, 0 ]

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
while x <= 200:
    y = math.floor(math.sqrt(200 - (x * x)))
    drawline(250, 250, x+250, y+250, screen, color)
    drawline(250, 250, x+250, 250-y, screen, color1)
    x+=1

display(screen)
save_extension(screen, 'img.png')
