import pygame as pg
from game.entities.player import players
from game.entities.simple_platform import Platform #rename to "[...].simple_platform due to pythons treatment to '-' sign"

class Game:
	def __init__(self):
		pg.init()
		self.screen = pg.display.set_mode((1280, 720), pg.SCALED, vsync=1)
		self.clock = pg.time.Clock()
    self.platforms = pygame.sprite.Group()
		self.platforms.add(
						Platform(
			            		 0,
		                 		 (self.screen.get_size()[1]//3)*2 ,
							     self.screen.get_size()[0],
						         self.screen.get_size()[1]//3
						        )
						)

	def run(self):
		dt = 0
		running = True
		while running:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					running = False
			
			players.update(dt)

			self.screen.fill("black")
      self.platforms.draw(self.screen)
			players.draw(self.screen)
			pg.display.flip()

			dt = self.clock.tick(60) / 1000
		pg.quit()

