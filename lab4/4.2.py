
import pygame
from pygame.draw import *


FPS = 30
BROWN_LIGHT = (101, 67, 33)
BROWN_DARK = (52, 28, 2)
ORANGE_DARK = (205, 87, 0)
ORANGE_LIGHT = (255, 162, 106)
GREY = (128, 128, 128)
GREY1 = (102, 102, 102)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE_LIGHT = (135, 206, 250)
BLUE_DARK = (0, 193, 255)
SCREEN_X = 600
SCREEN_Y = 600


def BackScreen (screen, x, y, bottm_clr, top_clr, y_divd):
    rect(screen, top_clr, (0, 0, x, y_divd))
    rect(screen, bottm_clr, (0, y_divd, x, y - y_divd))
def Window (screen, x_windw, y_windw, width_windw, height_windw, frame_clr, glass_clr):
    rect(screen, frame_clr, (x_windw, y_windw, width_windw, height_windw))
    rect(screen, glass_clr, (x_windw + 10, y_windw + 10, (width_windw - 30) / 2, (height_windw - 30) / 4))
    rect(screen, glass_clr, (x_windw + 20 + (width_windw - 30) / 2, y_windw + 10, (width_windw - 30) / 2, (height_windw - 30) / 4))
    rect(screen, glass_clr, (x_windw + 10, y_windw + 20 + (height_windw - 30) / 4, (width_windw - 30) / 2, 3 * (height_windw - 30) / 4))
    rect(screen, glass_clr, (x_windw + 20 + (width_windw - 30) / 2, y_windw + 20 + (height_windw - 30) / 4, (width_windw - 30) / 2, 3 * (height_windw - 30) / 4))
def Cats_Tale (x, y, width, height, cat_clr, right):
    surface = pygame.Surface((width / 2, height / 3), pygame.SRCALPHA)
    ellipse = pygame.draw.ellipse(surface, BLACK, (0, 0, width / 2, height / 3))
    ellipse = pygame.draw.ellipse(surface, cat_clr, (1, 1, width / 2 - 2, height / 3 - 2))
    surface = pygame.transform.rotate(surface, -15)
    if right:
        surface = pygame.transform.flip(surface, True, False)
        screen.blit(surface,(SCREEN_X - x - width, y + height / 9))
    else:
        screen.blit(surface,(x + width / 2, y + height / 9))
    pygame.display.update()
def Cats_Body (x, y, width, height, cat_clr, right):
    surface2 = pygame.Surface((1000, 800), pygame.SRCALPHA)
    ellipse = pygame.draw.ellipse(surface2, BLACK, (x + width / 7 - 1, y - 1, 2 * width / 3 + 2, 2 * height / 3 + 2))
    ellipse = pygame.draw.ellipse(surface2, cat_clr, (x + width / 7, y, 2 * width / 3, 2 * height / 3))
    ellipse = pygame.draw.ellipse(surface2, BLACK, (x + 4 * width / 50 - 1, y + 2 * height / 15 - 1, 2.5 * width / 25 + 2, 2.5 * height / 5 + 2))
    ellipse = pygame.draw.ellipse(surface2, cat_clr, (x + 4 * width / 50, y + 2 * height / 15, 2.5 * width / 25, 2.5 * height / 5))
    ellipse = pygame.draw.ellipse(surface2, BLACK, (x + 5 * width / 25 - 1, y + 11 * height / 21 - 1, 4 * width / 25 + 2, 4 * height / 21 + 2))
    ellipse = pygame.draw.ellipse(surface2, cat_clr, (x + 5 * width / 25, y + 11 * height / 21, 4 * width / 25, 4 * height / 21))
    ellipse = pygame.draw.ellipse(surface2, BLACK, (x + width / 50 - 1, y + height / 22 - 1, 11 * width / 50 + 2, 11 * width / 50 + 2))
    ellipse = pygame.draw.ellipse(surface2, cat_clr, (x + width / 50, y + height / 22, 11 * width / 50, 11 * width / 50))
    ellipse = pygame.draw.ellipse(surface2, BLACK, (x + 30 * width / 50 - 1, y + 7 * height / 21 - 1, 9 * width / 50 + 2, 10 * height / 21 + 2))
    ellipse = pygame.draw.ellipse(surface2, cat_clr, (x + 30 * width / 50, y + 7 * height / 21, 9 * width / 50, 10 * height / 21))
    ellipse = pygame.draw.ellipse(surface2, BLACK, (x + 36 * width / 50 - 1, y + 14 * height / 21 - 1, 3 * width / 50 + 2, 7 * height / 21 + 2))
    ellipse = pygame.draw.ellipse(surface2, cat_clr, (x + 36 * width / 50, y + 14 * height / 21, 3 * width / 50, 7 * height / 21))
    if right:
        surface2 = pygame.transform.flip(surface2, True, False)
    screen.blit(surface2,(0, 0))
    pygame.display.update()
def Cats_Ears (x, y, width, height, ear_clr, cat_clr, right):
    surface2 = pygame.Surface((1000, 800), pygame.SRCALPHA)
    polygon = pygame.draw.polygon(surface2, BLACK, ((x + 2 * width / 50, y + 5 * height / 21 + 1), (x + 5 * width / 50 + 2, y + 2 * height / 21 - 1), (x - 1, y + 1 * height / 21 - 1)))
    polygon = pygame.draw.polygon(surface2, cat_clr, ((x + 2 * width / 50, y + 5 * height / 21), (x + 5 * width / 50, y + 2 * height / 21), (x, y + 1 * height / 21)))
    polygon = pygame.draw.polygon(surface2, BLACK, ((x + 10 * width / 50, y + 5 * height / 21 + 2), (x + 7 * width / 50 - 2, y + 2 * height / 21 - 1), (x + 12 * width / 50 + 1, y + 1 * height / 21 - 1)))
    polygon = pygame.draw.polygon(surface2, cat_clr, ((x + 10 * width / 50, y + 5 * height / 21), (x + 7 * width / 50, y + 2 * height / 21), (x + 12 * width / 50, y + 1 * height / 21)))
    polygon = pygame.draw.polygon(surface2, BLACK, ((x + 2.25 * width / 50, y + 4 * height / 21 + 1), (x + 4 * width / 50 + 1, y + 2.25 * height / 21), (x + width / 60 - 1, y + 1.5 * height / 21 - 1)))
    polygon = pygame.draw.polygon(surface2, ear_clr, ((x + 2.25 * width / 50, y + 4 * height / 21), (x + 4 * width / 50, y + 2.25 * height / 21), (x + width / 60, y + 1.5 * height / 21)))
    polygon = pygame.draw.polygon(surface2, BLACK, ((x + 9.85 * width / 50, y + 4.125 * height / 21 + 1), (x + 8 * width / 50 - 2, y + 2.35 * height / 21 - 1), (x + 11.25 * width / 50 + 1, y + 1.5 * height / 21 - 1)))
    polygon = pygame.draw.polygon(surface2, ear_clr, ((x + 9.85 * width / 50, y + 4.125 * height / 21), (x + 8 * width / 50, y + 2.35 * height / 21), (x + 11.25 * width / 50, y + 1.5 * height / 21)))
    if right:
        surface2 = pygame.transform.flip(surface2, True, False)
    screen.blit(surface2,(0, 0))
    pygame.display.update()
def Cats_Eyes(x, y, width, height, eye_clr, cat_clr, look, right):
    surface2 = pygame.Surface((1000, 800), pygame.SRCALPHA)
    ellipse = pygame.draw.ellipse(surface2, BLACK, (x + 2.5 * width / 50 - 1, y + 5 * height / 22 - 1, 3 * width / 50 + 2, 3 * width / 50 + 2))
    ellipse = pygame.draw.ellipse(surface2, BLACK, (x + 6.5 * width / 50 - 1, y + 5 * height / 22 - 1, 3 * width / 50 + 2, 3 * width / 50 + 2))
    ellipse = pygame.draw.ellipse(surface2, eye_clr, (x + 2.5 * width / 50, y + 5 * height / 22, 3 * width / 50, 3 * width / 50))
    ellipse = pygame.draw.ellipse(surface2, eye_clr, (x + 6.5 * width / 50, y + 5 * height / 22, 3 * width / 50, 3 * width / 50))
    if look:
        ellipse = pygame.draw.ellipse(surface2, BLACK, (x + 4.25 * width / 50, y + 5.35 * height / 22, 0.5 * width / 50, 2.25 * width / 50))
        ellipse = pygame.draw.ellipse(surface2, BLACK, (x + 8.25 * width / 50, y + 5.35 * height / 22, 0.5 * width / 50, 2.25 * width / 50))
    else:
        ellipse = pygame.draw.ellipse(surface2, BLACK, (x + 3.25 * width / 50, y + 5.26 * height / 22, 0.5 * width / 50, 2.45 * width / 50))
        ellipse = pygame.draw.ellipse(surface2, BLACK, (x + 7.25 * width / 50, y + 5.26 * height / 22, 0.5 * width / 50, 2.45 * width / 50))
        if right:
            surface2 = pygame.transform.flip(surface2, True, False)
    screen.blit(surface2,(0, 0))
    pygame.display.update()
def Cats_Glare(x, y, width, height, look, right):
    surface2 = pygame.Surface(( 3 * width / 50, 3 * width / 50), pygame.SRCALPHA)
    ellipse = pygame.draw.ellipse(surface2, WHITE, ( 0 * width / 50,  0, 1.5 * width / 50, 0.5 * width / 50))
    surface2 = pygame.transform.rotate(surface2, -60)
    if right:
        screen.blit(surface2,(SCREEN_X - x - 5 * width / 50, y))
        surface2 = pygame.transform.flip(surface2, True, False)
    else:
        screen.blit(surface2,(x, y))
    pygame.display.update()
def Cats_Nose(x, y, width, height, ear_clr, right):
    surface2 = pygame.Surface((3 * width / 50, 3 * width / 50), pygame.SRCALPHA)
    polygon = pygame.draw.polygon(surface2, BLACK, ((0, 0), (2 + 1 * width / 50, 0), (1 + 0.5 * width / 50, 2 + 1 * height / 22)))
    polygon = pygame.draw.polygon(surface2, ear_clr, ((1, 1), (1 + 1 * width / 50, 1), (1 + 0.5 * width / 50, 1 + 1 * height / 22)))
    if right:
        screen.blit(surface2,(SCREEN_X - x - 1.5 * width / 50, y))
        surface2 = pygame.transform.flip(surface2, True, False)
    else:
        screen.blit(surface2,(x, y))
    pygame.display.update()
def Cats_Mouth(x, y, width, height, right):
    surface2 = pygame.Surface((6 * width / 50, 6 * width / 50), pygame.SRCALPHA)
    arc = pygame.draw.arc(surface2, BLACK, (0, 0, 2 * width / 50, 2 * width / 50), -3, 0)
    if right:
        screen.blit(surface2,(SCREEN_X - x - 1.5 * width / 50, y))
        surface2 = pygame.transform.flip(surface2, True, False)
    else:
        screen.blit(surface2,(x, y))
    pygame.display.update()
def Cats_Whiskers(x, y, width, height, right):
    surface2 = pygame.Surface((42 * width / 50, 42 * width / 50), pygame.SRCALPHA)
    arc = pygame.draw.arc(surface2, BLACK, (0, 0, 10 * width / 50, 5 * width / 50), 1.1, 2.5)
    arc = pygame.draw.arc(surface2, BLACK, (0, 0.5 * height / 22, 15 * width / 50, 10 * width / 50), 1.6, 2.5)
    arc = pygame.draw.arc(surface2, BLACK, (0, 1 * height / 22, 15 * width / 50, 17 * width / 50), 1.6, 2.5)
    arc = pygame.draw.arc(surface2, BLACK, (3 * width / 50, 0.125 * height / 22, 15 * width / 50, 5 * width / 50), 0.25, 1.3)
    arc = pygame.draw.arc(surface2, BLACK, (3 * width / 50, 0.25 * height / 22, 15 * width / 50, 8 * width / 50), 0.25, 1.3)
    arc = pygame.draw.arc(surface2, BLACK, (3 * width / 50, 0.5 * height / 22, 15 * width / 50, 12 * width / 50), 0.5, 1.3)
    if right:
        surface2 = pygame.transform.flip(surface2, True, False)
        screen.blit(surface2,(SCREEN_X - x - 40.5 * width / 50, y))
    else:
        screen.blit(surface2,(x, y))
    pygame.display.update()
def Ball(x, y, rad, right):
    surface2 = pygame.Surface((4 * rad, 2 * rad), pygame.SRCALPHA)
    ellipse = pygame.draw.ellipse(surface2, BLACK, (0, 0, 2 * rad, 2 * rad))
    ellipse = pygame.draw.ellipse(surface2, GREY, (1, 1, 2 * rad - 2, 2 * rad - 2))
    arc = pygame.draw.arc(surface2, BLACK, (-0.25 * rad, rad / 4, 2 * rad, 2 * rad), 0.5, 1.5)
    arc = pygame.draw.arc(surface2, BLACK, (-0.25 * rad, rad / 2, 2 * rad, 2 * rad), 0.5, 1.7)
    arc = pygame.draw.arc(surface2, BLACK, (-0.25 * rad, 3 * rad / 4, 2 * rad, 2 * rad), 0.5, 1.9)
    arc = pygame.draw.arc(surface2, BLACK, (0.5 * rad, rad / 2, 2 * rad, 2 * rad), 2.5, 3.3)
    arc = pygame.draw.arc(surface2, BLACK, (0.75 * rad, rad / 2, 2 * rad, 2 * rad), 2.5, 3.5)
    arc = pygame.draw.arc(surface2, BLACK, (1 * rad, rad / 2, 2 * rad, 2 * rad), 2.6, 3.5)
    arc = pygame.draw.arc(surface2, GREY, (0.65 * rad, 1.5 * rad, 8 * rad, 2 * rad), 2.1, 3.9)
    arc = pygame.draw.arc(surface2, GREY, (2 * rad, 1.58 * rad, 2 * rad, 2 * rad), 0, 1.97)
    if right:
        surface2 = pygame.transform.flip(surface2, True, False)
        screen.blit(surface2,(SCREEN_X - x - 4 * rad, y))
    else:
        screen.blit(surface2,(x, y))
    pygame.display.update()
def Cat (x, y, size, cat_clr, ear_clr, eye_clr, look, right):
    if right:
        look = not(look)
    width = size * 4.25;
    height = size * 2;
    surface2 = pygame.Surface((1000, 800), pygame.SRCALPHA)
    Cats_Tale(x, y, width, height, cat_clr, right)
    Cats_Body(x, y, width, height, cat_clr, right)
    Cats_Ears(x, y, width, height, ear_clr, cat_clr, right)
    Cats_Eyes(x, y, width, height, eye_clr, cat_clr, look, right)
    Cats_Glare(x + 1 * width / 50, y + 5 * height / 22, width, height, look, right)
    Cats_Glare(x + 5 * width / 50, y + 5 * height / 22, width, height, look, right)
    Cats_Nose(x + 5 * width / 50, y + 7.32 * height / 22, width, height, ear_clr, right)
    Cats_Mouth(x + 4 * width / 50, y + 7.32 * height / 22, width, height, right)
    Cats_Mouth(x + 6 * width / 50, y + 7.32 * height / 22, width, height, right)
    Cats_Whiskers(x - 3 * width / 50, y + 7.62 * height / 22, width, height, right)


pygame.init()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
BackScreen(screen, SCREEN_X, SCREEN_Y, BROWN_LIGHT, BROWN_DARK, 360)
Window(screen, 300, 40, 200, 250,  BLUE_LIGHT, BLUE_DARK)
Cat(100, 380, 100, ORANGE_DARK, ORANGE_LIGHT, GREEN, True, False)
Ball(250, 500, 40, False)

pygame.display.update()
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
