#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Импортируем библиотеку pygame
import pygame
from pygame import *
from player import *
from blocks import *
from monster import *


# Объявляем переменные
WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "black"


red = (200,0,0)
green = (0,200,0)
black = (0, 0, 0)
white = (255, 255, 255)
bright_red = (255,0,0)
bright_green = (0,255,0)

screen = pygame.display.set_mode(DISPLAY)
timer = pygame.time.Clock()


def quitgame():
    pygame.quit()
    quit()

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def button1(msg1,x,y,w,h,ic,ac,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # tworzenie przyciskow i ustawinie ich pozycji
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))


    # dodawanie textu dla przciskow
    smallText1 = pygame.font.SysFont('Arial', 25)
    TextSurf, TextRect = text_objects(msg1, smallText1)
    TextRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(TextSurf, TextRect)


def button2(msg2,x,y,w,h,ic,ac,action= None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText2 = pygame.font.SysFont('Arial', 25)
    TextSurf, TextRect = text_objects(msg2, smallText2)
    TextRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(TextSurf, TextRect)


def menu():
    intro = True
    pygame.mixer.music.load("awesomeness.wav")
    pygame.mixer.music.play(-1)
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(black)
        largeText = pygame.font.SysFont('Arial', 115)
        TextSurf, TextRect = text_objects("Jumper Racer", largeText)
        TextRect.center = ((WIN_WIDTH / 2), (WIN_HEIGHT / 4))
        screen.blit(TextSurf, TextRect)

        button1("Play",350,300,100,50, green, bright_green,main)
        button2("Quit", 350, 400, 100, 50, red, bright_red,quitgame)

        pygame.display.update()
        timer.tick(15)

pygame.init()


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

    l = min(0, l)  # Не движемся дальше левой границы
    l = max(-(camera.width - WIN_WIDTH), l)  # Не движемся дальше правой границы
    t = max(-(camera.height - WIN_HEIGHT), t)  # Не движемся дальше нижней границы
    t = min(0, t)  # Не движемся дальше верхней границы

    return Rect(l, t, w, h)



def main():
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Jumper Racer")  # Пишем в шапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом
    pygame.mixer.music.load("Caketown 1.mp3")
    pygame.mixer.music.play(-1)


    hero = Player(55, 55)  # создаем героя по (x,y) координатам
    left = right = False  # по умолчанию - стоим
    up = False
    mn3 = Monster(900, 565, 2, 3, 80, 10)
    mn4 = Monster(1600, 276, 2, 3, 100, 10)
    mn5 = Monster(2500, 465, 2, 3, 100, 10)
    mn6 = Monster(2900, 465, 2, 3, 100, 10)
    mn7 = Monster(4050, 565, 2, 3, 100, 10)
    entities = pygame.sprite.Group()  # всі обєкти
    monsters = pygame.sprite.Group()  # всі обєкти які рухаються
    animatedEntities = pygame.sprite.Group()
    platforms = []  # в то що вони будуть вдарятися або опиратися
    entities.add(hero)
    # твореня монстрів

    entities.add(mn3)
    platforms.append(mn3)
    monsters.add(mn3)

    entities.add(mn4)
    platforms.append(mn4)
    monsters.add(mn4)

    entities.add(mn5)
    platforms.append(mn5)
    monsters.add(mn5)

    entities.add(mn6)
    platforms.append(mn6)
    monsters.add(mn6)

    entities.add(mn7)
    platforms.append(mn7)
    monsters.add(mn7)

    # твореня порталів
    tp = BlockTeleport(324,122, 680, 1000)
    entities.add(tp)
    platforms.append(tp)
    animatedEntities.add(tp)


    tp1 = BlockTeleport(900, 122, 1300,1000)
    entities.add(tp1)
    platforms.append(tp1)
    animatedEntities.add(tp1)

    tp2 = BlockTeleport(1700, 142, 2280, 1000)
    entities.add(tp2)
    platforms.append(tp2)
    animatedEntities.add(tp2)

    tp3 = BlockTeleport(3400, 490, 3780, 1000)
    entities.add(tp3)
    platforms.append(tp3)
    animatedEntities.add(tp3)

    tp4 = BlockTeleport(4200, 490, 4480, 1000)
    entities.add(tp4)
    platforms.append(tp4)
    animatedEntities.add(tp4)

    level = [
        "---------------------------------------------------------------------------------------------------------------------------------------------------",
        "-   -               -                  -                            -                                         *-                                  -",
        "-   -               -                  -                            -                                         *-                                  -",
        "-   -               -                  -     -------------------    -                                         *-                                  -",
        "-   -               -                  -     -                      -               -----------------         *-                                  -",
        "-   -               -                  -  -  -                      -                               -         *-                                  -",
        "-   -               *                  -     -                      -                               -       * *-                                  -",
        "-   -               *                  -     -                      ---------                       -         *-                                  -",
        "-   -               *                  -    --                      -                               -         *-                                  -",
        "-   -     --        -                  -     -                      -        *                      -         *-                                  -",
        "-   -               -    ---           -     ---------              -              -                -         *-**********************************-",
        "-   -               -                  -     -                      -                               -   *     *-                        *         -",
        "-   -            -- -  **              - -   *                      -                *              -         *-                        *         -",
        "-                   -                  -     *                      -                         -     -         *-                        *         -",
        "-            --     -               *  -     *        * --          -                               -         *-                        *        &-",
        "-             *     -          ---     *                            -                               - *       *-                        *        --",
        "-       ---   *     -                  *   ----                  ----  ------------------------------         *-                        *      ----",
        "-   *         *     -                  *                            -                               -         *-                        *     -  --",
        "-   *         *     -   *              *****************************-**************************************** *-                        *    -   --",
        "---------------------------------------------------------------------------------------------------------------------------------------------------"]

    timer = pygame.time.Clock()
    x = y = 0  # координаты
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "*":
                bd = BlockDie(x,y)
                entities.add(bd)
                platforms.append(bd)
            if col == "&":
                pr = Princess(x, y)
                entities.add(pr)
                platforms.append(pr)


            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля

    total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
    total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

    camera = Camera(camera_configure, total_level_width, total_level_height)

    while 1:  # Основной цикл программы
        timer.tick(60)
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == QUIT:
                raise SystemExit, "QUIT"
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
        monsters.update(platforms)  # рух монстрів
        animatedEntities.update()
        camera.update(hero)  # центризируем камеру относительно персонажа
        hero.update(left, right, up, platforms)  # передвижение
        # entities.draw(screen) # отображение
        for e in entities:
            screen.blit(e.image, camera.apply(e))

        pygame.display.update()  # обновление и вывод всех изменений на экран



menu()
if __name__ == "__main__":
    main()
