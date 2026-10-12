import pygame

class Player:
	def __init__(self, color, position: pygame.Vector2, dimentions: pygame.Vector2):
		self.position = position
		self.image = pygame.Surface([dimentions.x, dimentions.y])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.center = self.position

