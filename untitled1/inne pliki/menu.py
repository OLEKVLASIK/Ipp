#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import pygame
#import mar

#red = (200,0,0)
#green = (0,200,0)
#black = (0, 0, 0)
#white = (255, 255, 255)#

#bright_red = (255,0,0)
#bright_green = (0,255,0)

#WIN_WIDTH = 800  # Ширина создаваемого окна
#WIN_HEIGHT = 640  # Высота
#DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
#BACKGROUND_COLOR = "black"
#screen = pygame.display.set_mode(DISPLAY)
#timer = pygame.time.Clock()


#def text_objects(text, font):
 #   textSurface = font.render(text, True, white)
  #  return textSurface, textSurface.get_rect()

#def button1(msg1,x,y,w,h,ic,ac,action = None):
 #   mouse = pygame.mouse.get_pos()

  #  click = pygame.mouse.get_pressed()

   # # tworzenie przyciskow i ustawinie ich pozycji
    #if x + w > mouse[0] > x and y + h > mouse[1] > y:
     #   pygame.draw.rect(screen, ac, (x, y, w, h))
      #  if click[0] == 1 and action != None:
       #     if action == "Play":
        #        print "gramy"#fukcja gry
         #   elif action == "Quit":
          #      raise SystemExit,"Quit"
    #else:
     #   pygame.draw.rect(screen, ic, (x, y, w, h))


    # dodawanie textu dla przciskow
    #smallText1 = pygame.font.SysFont('Arial', 25)
    #TextSurf, TextRect = text_objects(msg1, smallText1)
    #TextRect.center = ((x + (w / 2)), (y + (h / 2)))
    #screen.blit(TextSurf, TextRect)


#def button2(msg2,x,y,w,h,ic,ac,action):

#    mouse = pygame.mouse.get_pos()

 #   if x + w > mouse[0] > x and y + h > mouse[1] > y:
  #      pygame.draw.rect(screen, ac, (x, y, w, h))
   # else:
    #    pygame.draw.rect(screen, ic, (x, y, w, h))

    #smallText2 = pygame.font.SysFont('Arial', 25)
    #TextSurf, TextRect = text_objects(msg2, smallText2)
    #TextRect.center = ((x + (w / 2)), (y + (h / 2)))
    #screen.blit(TextSurf, TextRect)


#def game_intro():
 #   intro = True

#    while intro:
 #       for event in pygame.event.get():
  #          print(event)
   #         if event.type == pygame.QUIT:
    #            pygame.quit()
     #           quit()

#        screen.fill(black)
 #       largeText = pygame.font.SysFont('Arial', 115)
  #      TextSurf, TextRect = text_objects("Jumper Racer", largeText)
    #    TextRect.center = ((WIN_WIDTH / 2), (WIN_HEIGHT / 4))
   #     screen.blit(TextSurf, TextRect)

     #  button1("Play",350,300,100,50, green, bright_green,"Play")
      #  button2("Quit", 350, 400, 100, 50, red, bright_red,"Quit")

      #  pygame.display.update()
       # timer.tick(15)


#pygame.init()
#game_intro()
