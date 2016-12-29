#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pygame import *
import pyganim
import os
import blocks
import monster
import sys



MOVE_SPEED=7
WIDTH= 45
HEIGHT=53
COLOR="blue"
JUMP_POWER = 10
GRAVITY = 0.35
ANIMATION_DELAY = 0.1#zmiana animacji
ICON_DIR = os.path.dirname(__file__)


ANIMATION_RIGHT = [('%s/postac/12.png' % ICON_DIR),
            ('%s/postac/13.png' % ICON_DIR),
            ('%s/postac/14.png' % ICON_DIR),
            ('%s/postac/15.png' % ICON_DIR),
            ('%s/postac/16.png' % ICON_DIR),
            ('%s/postac/17.png' % ICON_DIR),
            ('%s/postac/18.png' % ICON_DIR),
            ('%s/postac/19.png' % ICON_DIR),
            ('%s/postac/20.png' % ICON_DIR)]
ANIMATION_LEFT = [('%s/postac/9.png' % ICON_DIR),
            ('%s/postac/1.png' % ICON_DIR),
            ('%s/postac/2.png' % ICON_DIR),
            ('%s/postac/3.png' % ICON_DIR),
            ('%s/postac/4.png' % ICON_DIR),
            ('%s/postac/5.png' % ICON_DIR),
            ('%s/postac/6.png' % ICON_DIR),
            ('%s/postac/7.png' % ICON_DIR),
            ('%s/postac/8.png' % ICON_DIR)]
ANIMATION_JUMP_LEFT = [('%s/postac/22.png' % ICON_DIR, 0.1)]
ANIMATION_JUMP_RIGHT = [('%s/postac/35.png' % ICON_DIR, 0.1)]
ANIMATION_JUMP = [('%s/postac/31.png' % ICON_DIR, 0.1)]
ANIMATION_STAY = [('%s/postac/21.png' % ICON_DIR, 0.1)]





class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel=0# скорість переміщеня,0-стоїмо на місці
        self.yvel=0
        self.startX=x#початкова позиція х,
        self.startY=y
        self.image=Surface((WIDTH,HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect=Rect(x,y,WIDTH,HEIGHT)#прямокутний обєкт
        self.onGround=False
        self.image.set_colorkey(Color(COLOR)) #przezroczysty fon


        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()#

        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        self.boltAnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()

        self.boltAnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()

        self.boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play()



    def update(self,left,right,up, platforms):
        if up:
            if self.onGround:
                self.yvel=-JUMP_POWER
            self.image.fill(Color(COLOR))
            self.boltAnimJump.blit(self.image, (0, 0))

        if left:
            self.xvel=-MOVE_SPEED #ліво =x-n
            self.image.fill(Color(COLOR))
            if up:  # для прыжка влево есть отдельная анимация
                self.boltAnimJumpLeft.blit(self.image, (0, 0))
            else:
                self.boltAnimLeft.blit(self.image, (0, 0))

        if right:
            self.xvel=MOVE_SPEED#право = x+n
            self.image.fill(Color(COLOR))
            if up:
                self.boltAnimJumpRight.blit(self.image, (0, 0))
            else:
                self.boltAnimRight.blit(self.image, (0, 0))

        if not(left or right):#cтоїмо коли нема наказу йти
            self.xvel=0
            if not up:
               self.image.fill(Color(COLOR))
               self.boltAnimStay.blit(self.image, (0, 0))


        if not self.onGround:
            self.yvel+=GRAVITY

        self.onGround=False
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)


    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if isinstance(p, blocks.BlockDie)or isinstance(p, monster.Monster):
                    self.die()
                elif isinstance(p,blocks.BlockTeleport):
                    self.teleporting(p.goX,p.goY)
                elif isinstance(p, blocks.Princess):  # якшо торкнувся принцеси виграв
                    print "wygrales"
                    sys.exit()

                if xvel > 0:
                    self.rect.right=p.rect.left
                if xvel < 0:
                    self.rect.left=p.rect.right
                if yvel > 0:
                    self.rect.bottom=p.rect.top
                    self.onGround=True
                    self.yvel=0
                if yvel < 0:
                    self.rect.top=p.rect.bottom
                    self.yvel=0


    def die(self):
        time.wait(500)
        self.teleporting(self.startX, self.startY)# przemieszczamy w poczatkowe miejsce

    def teleporting(self, goX, goY):
        self.rect.x=goX
        self.rect.y=goY


