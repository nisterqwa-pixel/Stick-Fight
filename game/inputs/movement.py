import pygame as pg

def check_movement_input(player):
	keys = pg.key.get_pressed()

	if keys[pg.K_a]:
		player.velocity.x = -550
	if keys[pg.K_d]:
		player.velocity.x = 550
	if keys[pg.K_w]:
		player.velocity.y = -550
	if keys[pg.K_s]:
		player.velocity.y = 550
	
	if not keys[pg.K_a] and not keys[pg.K_d]:
		player.velocity.x = 0
	if not keys[pg.K_w] and not keys[pg.K_s]:
		player.velocity.y = 0

	
