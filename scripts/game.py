import pygame, os
from scripts.sprite import Sprite
from scripts.constants import display_size
from scripts.functions import load_image
from scripts.player import Player
from scripts.platform import Platform
from scripts.platform_generator import PlatformGenerator
class Game():
    def __init__(self):
        self.background_image=pygame.image.load(os.path.join('assets','images','background.png'))
        self.platform_generator = PlatformGenerator(200)
        self.player=Player((240,600),load_image('assets','images','player.png'),5,20,0.65)
        self.platforms=list()

        self.offset_y=0
    def render(self,surface:pygame.Surface):
        surface.blit(self.background_image, (0,0))
        for platform in self.platforms:
            platform.render(surface,self.offset_y)
        self.player.render(surface,self.offset_y)
    def handle_key_down_event(self,key):
        if key == pygame.K_a:
            self.player.is_walking_left=True
        elif key == pygame.K_d:
            self.player.is_walking_right=True
    def handle_key_up_event(self,key):
        if key == pygame.K_a:
            self.player.is_walking_left=False
        elif key == pygame.K_d:
            self.player.is_walking_right=False
    def handle_create_platform_event(self,platform):
        self.platforms.append(platform)
    def update(self):
        self.player.update()
        for platform in self.platforms:
            if self.player.collide_sprite(platform):
                self.player.on_platform=True
        if self.player.rect.bottom - self.offset_y<display_size[1]/3:
            self.offset_y=self.player.rect.bottom-display_size[1]/3
        self.platform_generator.update(self.offset_y,self.platforms)
        print(self.offset_y)