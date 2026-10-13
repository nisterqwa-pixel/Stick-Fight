import pygame as pg

class Player:
	def __init__(self, color, position: pg.Vector2, dimentions: pg.Vector2):
		self.position = position
		self.image = pg.Surface([dimentions.x, dimentions.y])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.center = self.position

