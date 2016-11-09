#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame import *
from player import *
from blocks import *


WIN_WIDTH =800 #ширина
WIN_HEIGHT=650 #висота
DISPLAY=(WIN_WIDTH,WIN_HEIGHT) #групировка
BACKGROUND_COLOR="black" #колір тла
PLATFORM_WIDTH=32
PLATFORM_HEIGHT=32
PLATFORM_COLOR="yellow"



def main():
    pygame.init()# ініціалізація pygame
    screen = pygame.display.set_mode(DISPLAY) #cтворюєм вікно
    pygame.display.set_caption("Mario")# назва вікна
    bg=Surface((WIN_WIDTH,WIN_HEIGHT))# створеня видимої поверхні

    bg.fill(Color(BACKGROUND_COLOR)) #заливаєм її коліром
    hero=Player(55,55)# створюєм героя(х,y)
    left=right=False# стоїмо якшо нічого не робимо
    up=False
    entities = pygame.sprite.Group()
    platforms = []
    entities.add(hero)
    level = [
       "-------------------------",
       "-                       -",
       "-                       -",
       "-                       -",
       "-            --         -",
       "-                       -",
       "--                      -",
       "-                       -",
       "-                   --- -",
       "-                       -",
       "-                       -",
       "-      ---              -",
       "-                       -",
       "-   -----------         -",
       "-                       -",
       "-                -      -",
       "-                   --  -",
       "-                       -",
       "-                       -",
       "-------------------------"] #рівеень

    timer = pygame.time.Clock()
    x=y=0 #координати
    for row in level: #весь рядок
            for col in row:# кожен символ
                if col == "-":
                    pf = Platform(x,y)
                    entities.add(pf)
                    platforms.append(pf)
                x=x+PLATFORM_WIDTH# блоки платформи ставляться на ширині блоків
            y=y+PLATFORM_HEIGHT# то саме і з висотою
            x=0 #на кожному рядку починаєм з нуля



    while 1: #основний цикл програми
        timer.tick(60)
        for i in pygame.event.get():
            if i.type==QUIT:
                raise SystemExit,"QUIT"

            if i.type == KEYDOWN and i.key == K_UP:
                up = True
            if i.type == KEYDOWN and i.key == K_LEFT:
                left = True
            if i.type == KEYDOWN and i.key == K_RIGHT:
                right = True

            if i.type == KEYUP and i.key == K_UP:
                up = False
            if i.type == KEYUP and i.key == K_RIGHT:
                right = False
            if i.type == KEYUP and i.key == K_LEFT:
                left = False


        screen.blit(bg,(0,0)) #кожну ітерацію треба все перремальовувати
        hero.update(left, right, up,platforms)# рух
        entities.draw(screen) #відображеня




        pygame.display.update() # обновлення і вивід всіх змін на екран



if __name__ == "__main__":
    main()
