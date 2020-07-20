import pygame
from display import Display


class App:
    def __init__(self):
        self.size = self.width, self.height = 800, 600
        self._running = True
        self._display = None
        self._window = None
        self._clock = None

    def load_window(self):
        pygame.init()
        self._window = pygame.display.set_mode(self.size)
        self._display = Display([800, 600])
        self._clock = pygame.time.Clock()
        self._running = True

    def update(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.MOUSEMOTION:
            self._display.update(event)

    def render(self):
        self._display.render()
        self._window.blit(self._display.get_image(self.size), [0, 0])
        pygame.display.flip()

    def dispose(self):
        self._running = False
        pygame.quit()

    def run(self):
        self.load_window()
        while self._running:
            self._clock.tick(60)
            for event in pygame.event.get():
                self.update(event)
            self.render()


if __name__ == '__main__':
    App().run()
