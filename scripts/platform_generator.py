from random import *
from scripts.platform import Platform
import pygame
from scripts.constants import display_size,CreatePlatformEvent
from scripts.functions import load_image
class PlatformGenerator():
    def __init__(self,step):
        self.step=step
        self.platform_images = [
            load_image('assets','images','platform.png'),
            load_image('assets','images','breaking-platform.png'),
            load_image('assets','images','platform.png'),
            load_image('assets','images','moving-platform.png')
        ]
        self.create_start_configuration()
    def create_start_configuration(self):
        
        event=pygame.Event(CreatePlatformEvent,{'platform':Platform((display_size[0]/2,display_size[1]-50),self.platform_images[0])})
        pygame.event.post(event)
        for y in range(int(display_size[1]/self.step),-1,-1):
            self.create_platform(y*self.step)
    def create_platform(self,center_y):
        number=randint(0,3)
        image=self.platform_images[number]
        min_x=image.get_width()//2
        max_x=display_size[0]-image.get_width()//2
        center=(randint(min_x,max_x),center_y)
        event=pygame.Event(CreatePlatformEvent,{'platform':Platform(center,image)})
        pygame.event.post(event)
        
    def update(self,offset_y,platforms):
        if platforms[-1].rect.centery-offset_y>=self.step:
            self.create_platform(offset_y)
            platforms.remove(platforms[0])