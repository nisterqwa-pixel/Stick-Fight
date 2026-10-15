import pygame
from game.entities.simple_platform import Platform #rename to "[...].simple_platform due to pythons treatment to '-' sign"

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((1280, 720), pygame.SCALED, vsync=1)
		self.clock = pygame.time.Clock()
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
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
			
			self.screen.fill("black")
			self.platforms.draw(self.screen)
			pygame.display.flip()
			dt = self.clock.tick(60) / 1000

		pygame.quit()

