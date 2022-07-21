import sys, pygame
# a function that will draw a right-angled triangle of a given size anchored at a given location
def draw_triangle(screen, x, y, size):
    pygame.draw.polygon(screen, white, [[x, y], [x + size, y], [x, y - size]])
def sierpinski(screen, x, y, size):
    mini_size = 10
    if size < mini_size:
        return draw_triangle(screen, x, y, size)
    else:
        new_size = int(size*0.5)
        draw_triangle(screen, x, y, new_size)
        sierpinski(screen,x, y,new_size)
        sierpinski(screen, x, y-new_size,new_size)
        sierpinski(screen, x+new_size, y,new_size )
