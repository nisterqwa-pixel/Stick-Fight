import pygame as pg
import game.constants as constants
from game.inputs.movement import check_movement_input

class Player(pg.sprite.Sprite):
	def __init__(self, color, position: pg.Vector2, dimentions: pg.Vector2):
		super().__init__()
		self.position = position
		self.direction = pg.Vector2(0, 0)

		self.image = pg.Surface([dimentions.x, dimentions.y])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.center = self.position

	def update(self, dt):
		check_movement_input(self)
		self.position += self.direction * constants.SPEED * dt
		self.rect.center = self.position

players = pg.sprite.Group()
player1 = Player(
	color		= "red",
	position	= pg.Vector2(1280 / 2, 720 / 2),
	dimentions	= pg.Vector2(60, 60)
)
players.add(player1)