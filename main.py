from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
color1 = [ 255, 0, 0 ]

draw_line(250,250,300,500,screen,color)
plot(screen,color1,300,500)
draw_line(250,250,500,400,screen,color)
plot(screen,color1,500,400)
draw_line(250,250,250,400,screen,color)
plot(screen,color1,250,400)
draw_line(250,250,500,250,screen,color)
plot(screen,color1,500,250)
#draw_line(250,250,100,350,screen,color)
#plot(screen,color1,100,350)
#draw_line(250,250,200,400,screen,color)
#plot(screen,color1,200,400)

display(screen)
save_extension(screen, 'img.png')
