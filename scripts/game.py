import pygame, os
from scripts.sprite import Sprite
from scripts.functions import load_image
class Game():
    def __init__(self):
        self.background_image=pygame.image.load(os.path.join('assets','images','background.png'))
        self.player=Sprite((240,600),load_image('assets','images','player.png'),)
    def render(self,surface:pygame.Surface):
        surface.blit(self.background_image, (0,0))
        self.player.render(surface)
