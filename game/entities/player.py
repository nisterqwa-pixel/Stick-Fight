import pygame as pg
import game.constants as constants

class Player(pg.sprite.Sprite):
	def __init__(self, color, position: pg.Vector2, dimentions: pg.Vector2):
		super.__init__()
		self.position = position
		self.velocity = pg.Vector2(0, 0)

		self.image = pg.Surface([dimentions.x, dimentions.y])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.center = self.position

	def update(self, dt):
		self.velocity.y += constants.GRAVITY * dt
		self.position += self.velocity * dt
		self.rect.center = self.position
