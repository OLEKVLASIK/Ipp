from pygame import *
import os
import monster
import pyganim


PLATFORM_WIDTH=32
PLATFORM_HEIGHT=32
PLATFORM_COLOR="yellow"

ICON_DIR  = os.path.dirname(__file__)

ANIMATION_BLOCKTELEPORT = [
    ('%s/blocks/port2.png' % ICON_DIR),
    ('%s/blocks/port1.png' % ICON_DIR)]


class Platform(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH,PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("%s/blocks/platform.png" % ICON_DIR)
        self.rect = Rect(x,y, PLATFORM_HEIGHT,PLATFORM_WIDTH)

class BlockDie(Platform):
    def __init__(self,x,y):
        Platform.__init__(self,x,y)
        self.image = image.load("%s/blocks/dieBlock.png" % ICON_DIR)

class Princess(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x,y)
        self.image = image.load("%s/blocks/princess.png" % ICON_DIR)


class BlockTeleport(Platform):
    def __init__(self, x, y, goX, goY):
        Platform.__init__(self, x, y)
        self.goX = goX
        self.goY = goY
        boltAnim = []
        for anim in ANIMATION_BLOCKTELEPORT:
            boltAnim.append((anim, 0.3))
        self.boltAnim = pyganim.PygAnimation(boltAnim)
        self.boltAnim.play()

    def update(self):
        self.image.fill(Color(PLATFORM_COLOR))
        self.boltAnim.blit(self.image, (0, 0))