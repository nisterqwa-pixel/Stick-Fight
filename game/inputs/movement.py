import pygame as pg
from math import sqrt

def check_movement_input(player):
	keys = pg.key.get_pressed()

	if keys[pg.K_a]:
		player.direction.x += -1
	if keys[pg.K_d]:
		player.direction.x += 1
	if keys[pg.K_w]:
		player.direction.y += -1
	if keys[pg.K_s]:
		player.direction.y += 1

	if not keys[pg.K_a] and not keys[pg.K_d]:
		player.direction.x = 0
	if not keys[pg.K_w] and not keys[pg.K_s]:
		player.direction.y = 0

	normalize_vector(player.direction)

def normalize_vector(direction: pg.Vector2):
	magnitude = sqrt(direction.x**2 + direction.y**2)
	if magnitude != 0:
		direction.x /= magnitude
		direction.y /= magnitude
