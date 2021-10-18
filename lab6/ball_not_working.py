import pygame
import math
from pygame.draw import *
from random import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 900))

number_of_balls = 3

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]



def new_ball():
    global x, y, r, color
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


    
def move1():
    global x, y, Vx, Vy, dt
    
    if (x+r>=1200):
        Vx=int(-Vx - randint(-3,3))
        if (abs(Vx>5)):
            Vx=5
        if (abs(Vx<0)):
            Vx=-4
    if (x-r<=0):
        Vx=int(-Vx - randint(-3,3))
        if (abs(Vx>5)):
            Vx=5
        if (abs(Vx<0)):
            Vx=4
    
    if (y+r>=900):
        Vy=int(-Vy - randint(-3,3))
        if (abs(Vy>5)):
            Vy=5
        if (abs(Vy<0)):
            Vy=-4
    if (y-r<=0):
        Vy=int(-Vy - randint(-3,3))
        if (abs(Vy>5)):
            Vy=5
        if (abs(Vy<0)):
            Vy=4
    
    x=x+Vx*dt    
    y=y+Vy*dt


def move2():
    global x, y, Vx, Vy, dt, a, Vy1
    a=5
    
    Vy1=Vy-a*dt
    Vy=Vy1
    
    x=x+Vx*dt
    y=y-V1y*dt+a*dt*dt/2
    
    print(Vy)
    if (y+r>=900):
        Vy1=-1*Vy1
        y=y-r/2
    
    if (x+r>=1200):
        Vx=-Vx
        x=x-10
    if (x-r<=0):
        Vx=-Vx
        x=x+10


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



"pool = [ball for i in range (number_of_balls)]"


k=0

br2=0
while (br2!=1):
    br1=0
    
    clock.tick(FPS)
    
    new_ball()
    
    Vx=randint(-3,3)
    Vy=randint(-3,3)
    
    while (br==0):
        move2()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inside()==True:
                    br1=1
                    k=k+1
                    print("Your score is", k)
                    print()
                else:
                    br1=0
                    print("Your score is still", k)
                    print()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if (br1==1):
                break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                br2=1
                break
        if event.type == pygame.QUIT:
            br2=1
            break
                
        circle(screen, color, (int(x), int(y)), r)
        pygame.display.update()
        screen.fill(BLACK)

pygame.quit()
