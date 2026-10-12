import pygame

class Player:
	def __init__(self, color, position: pygame.Vector2, dimentions: pygame.Vector2):
		self.color = color
		self.postion = position
		self.dimentions = dimentions

