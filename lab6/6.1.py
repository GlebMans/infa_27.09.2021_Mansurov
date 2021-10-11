import pygame
import math
from pygame.draw import *
from random import randint
pygame.init()

FPS = 0.7
screen = pygame.display.set_mode((1200, 900))

number of balls = 3

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def click(event):
    print(x, y, r)

def inside():
    mx,my=pygame.mouse.get_pos()
    rtx=mx-x
    rty=my-y
    if math.sqrt(math.pow(rtx,2)+math.pow(rty,2))<=r:
        print('Great!')
        return True
    else:
        print('Oof...')
        return False

pygame.display.update()
clock = pygame.time.Clock()
finished = False

k=0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if inside()==True:
                k=k+1
                print("Your score is", k)
                print()
            else:
                print("Your score is still", k)
                print()
    
    
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
