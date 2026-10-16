import pygame
import game.constants as CONSTANTS

class Platform(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill('#808089')
        self.rect = self.image.get_rect()
        self.rect.y = yloc 
        self.rect.x = xloc 
        
platforms = pygame.sprite.Group()
winsz = ()
  
platform1 = Platform(
	0,
	(CONSTANTS.SCREEN["height"]//3)*2 ,
	CONSTANTS.SCREEN["width"],
 	CONSTANTS.SCREEN["height"]//3
)     
platforms.add(platform1)
