from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line(250,250,300,500,screen,color)
draw_line(250,250,500,400,screen,color)
display(screen)
save_extension(screen, 'img.png')
