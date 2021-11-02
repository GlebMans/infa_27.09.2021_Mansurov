import pygame
import math
from pygame.draw import *
from random import *
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 600))

number_of_balls = 10

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]



balls=[]

class Ball:
    def __init__(self, x, y, r, color):
        self.x=randint(30,1150)
        self.y=randint(30,550)
        self.r=randint(30,50)
        self.color=COLORS[randint(0, 5)]
        self.Vx = randint(-5,5)
        self.Vy = randint(-5,5)
        self.a = 1
        self.dt = 1

        j = randint(0,1)

        if j == 0:
            self.move = self.move1
            self.score=10
        if j == 1:
            self.move = self.move2
            self.score=25

 
    def move1(self):
        x, y, r, Vx, Vy, dt, a=self.x, self.y, self.r, self.Vx, self.Vy, self.dt, self.a
        
        if (x+r>=1200):
            Vx=V_higher(Vx)
        if (x-r<=0):
            Vx=V_lower(Vx)

        if (y+r>=600):
            Vy=V_higher(Vy)
        if (y-r<=0):
            Vy=V_lower(Vy)

        x=x+Vx*dt    
        y=y+Vy*dt

        self.x, self.y, self.Vx, self.Vy, self.dt = x, y, Vx, Vy, dt


    def move2(self):
        x, y, Vx, Vy, r, dt, a= self.x, self.y, self.Vx, self.Vy, self.r, self.dt, self.a
        dt=1
        a=1
    
        if (y+r>=600):
            Vy=-Vy
    
        if (x+r>=1200):
            Vx=V_higher(Vx)
        if (x-r<=0):
            Vx=V_lower(Vx)

        x=x+Vx*dt
        y=y-Vy*dt+a*dt*dt/2
    
        Vy=Vy-a*dt

        self.x, self.y, self.Vx, self.Vy=x, y, Vx, Vy
    
    def draw(self, screen):
        circle(screen, self.color, (self.x, self.y), self.r)


def V_border(V):
    if (V>5):
        V=3

def V_lower(V):
    V=int(-V - randint(-5,5))
    if (V<0):
        V=randint(1,5)
    V_border(V)
    return V

def V_higher(V):
    V=int(-V - randint(-5,5))
    if (V>0):
        V=randint(1,5)
    V_border(V)
    return V


def new_ball():
    global COLORS
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    balls.append(Ball(x, y, r, color))


def create():
    for i in range(number_of_balls):
        new_ball()
create()

score=0
def kill(find):
    global score
    find=find[::-1]
    for i in find:
        score += balls[i].score
        del balls[i]
        new_ball()
       
        print("Great! Your score is", score)
    


def inside():
    mx,my=pygame.mouse.get_pos()
    find = []
    for i in range(len(balls)):
        x = balls[i].x
        y = balls[i].y
        r = balls[i].r

        if (x-mx)**2+(y-my)**2<r**2:
            find.append(i)
    return find

def update():
    for i in range(len(balls)):
        balls[i].move2()
        balls[i].draw(screen)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

br2=0
while (br2!=1):
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            kill(inside())
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                br2=1
        if event.type == pygame.QUIT:
            br2=1       
    update()

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
