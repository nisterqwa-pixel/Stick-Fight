import pygame as pg
from game.entities.player import players
from game.entities.simple_platform import platforms  #rename to "[...].simple_platform due to pythons treatment to '-' sign"

class Game:
	def __init__(self):
		pg.init()
		self.screen = pg.display.set_mode((1280, 720), pg.SCALED, vsync=1)
		self.clock = pg.time.Clock()
       
 


	def run(self):
		dt = 0
		running = True

  
		while running:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					running = False

			players.update(dt)

			self.screen.fill("black")
			platforms.draw(self.screen)
			players.draw(self.screen)
			pg.display.flip()

			dt = self.clock.tick(60) / 1000

		pg.quit()
  