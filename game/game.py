import pygame

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((1280, 720), pygame.SCALED, vsync=1)
		self.clock = pygame.time.Clock()

	def run(self):
		dt = 0
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
			
			self.screen.fill("black")
			pygame.display.flip()
			dt = self.clock.tick(60) / 1000

		pygame.quit()

