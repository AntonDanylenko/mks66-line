from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
color1 = [ 255, 0, 0 ]
color2 = [ 0, 0, 255 ]

#oct 1
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

display(screen)
save_extension(screen, 'img.png')
