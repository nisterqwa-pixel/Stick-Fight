import pygame as pg

class Player(pg.sprite.Sprite):
	def __init__(self, color, position: pg.Vector2, dimentions: pg.Vector2):
		super.__init__()
		self.position = position
		self.velocity = pg.Vector2(0, 0)

		self.image = pg.Surface([dimentions.x, dimentions.y])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.center = self.position

