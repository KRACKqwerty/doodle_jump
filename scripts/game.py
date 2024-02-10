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
        self.losed=False
        self.font=pygame.Font(os.path.join('assets','fonts','pixel.ttf'),32)

        self.offset_y=0
    def render(self,surface:pygame.Surface):
        surface.blit(self.background_image, (0,0))
        for platform in self.platforms:
            platform.render(surface,self.offset_y)
        self.player.render(surface,self.offset_y)
        score=round(-self.offset_y/10)
        if self.losed:
            score_text=self.font.render(f'Ваш рекорд: {score}',True,(1,1,1))
            hint_text=self.font.render('Нажмите любую кнопку',True,(1,1,1))

            score_rect=score_text.get_rect(centerx=display_size[0]/2,centery=display_size[1]/2-25)
            hint_rect=hint_text.get_rect(centerx=display_size[0]/2,centery=display_size[1]/2+25)

            surface.blit(score_text,score_rect)
            surface.blit(hint_text,hint_rect)
        else:
            text=self.font.render(str(score),True,(1,1,1))
            rect=text.get_rect(midtop=(display_size[0]/2,10))
            surface.blit(text,rect)

    def handle_key_down_event(self,key):
        if self.losed:
            self.restart()
        elif key == pygame.K_a:
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

    def restart(self):

        self.losed=False
        self.offset_y=0
        self.platforms=list()
        self.platform_generator.create_start_configuration()

    def update(self):
        self.losed = self.player.rect.top - self.offset_y >= display_size[1]
        if self.losed:
            return
        self.player.update()
        for platform in self.platforms:
            if self.player.collide_sprite(platform):
                self.player.on_platform=True
        if self.player.rect.bottom - self.offset_y<display_size[1]/3:
            self.offset_y=self.player.rect.bottom-display_size[1]/3
        if self.platforms:
            self.platform_generator.update(self.offset_y,self.platforms)
        