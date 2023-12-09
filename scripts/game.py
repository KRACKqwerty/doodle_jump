import pygame, os
class Game():
    def __init__(self):
        self.background_image=pygame.image.load(os.path.join('assets','images','background.png'))
    def render(self,surface:pygame.Surface):
        surface.blit(self.background_image, (0,0))