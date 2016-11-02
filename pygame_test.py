import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREEN_SIZE = (700, 500)


class Game:
	def __init__(self, screenSurface):
		self.screen = screenSurface
		self.quit = False
		self.fps = 60
		self.clock = pygame.time.Clock()
	
	def process_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quit = True
	
	def run_logic(self):
		pass

	def render(self):
		self.screen.fill(WHITE)
		pygame.draw.circle(self.screen, BLACK, (300, 300), 10)
		pygame.display.flip()

	def run(self):
		while not self.quit:
			self.process_events()
			self.run_logic()
			self.render()
			self.clock.tick(self.fps)


def main():
	pygame.init()
	screen = pygame.display.set_mode(SCREEN_SIZE)
	pygame.display.set_caption("Game")
	game = Game(screen)
	print("Running the game")
	game.run()


if __name__ == "__main__":
	main()
