import pygame as pg
import game.constants as CONSTANTS
from math import sqrt

def check_movement_input(player):
	keys = pg.key.get_pressed()

	# this only applies for 8-direction-movement
	player.direction.x = keys[pg.K_d] - keys[pg.K_a]
	player.direction.y = keys[pg.K_s] - keys[pg.K_w]

	normalize_vector(player.direction)

	player.velocity.x = player.direction.x * CONSTANTS.SPEED
	player.velocity.y = player.direction.y * CONSTANTS.SPEED

def normalize_vector(direction: pg.Vector2):
	magnitude = sqrt(direction.x**2 + direction.y**2)
	if magnitude != 0:
		direction.x /= magnitude
		direction.y /= magnitude
