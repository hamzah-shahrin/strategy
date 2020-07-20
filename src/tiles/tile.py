import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, color=None, image=None, callback=None):
        super().__init__()
        self.name = "Default Tile"
        self.image = pygame.Surface([8, 8])
        self.color = color
        self.image.blit(image, [0, 0]) if image else self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.callback = callback

    def set_pos(self, pos):
        self.rect.x, self.rect.y = pos

    def update(self, event):
        if self.rect.collidepoint([event.pos[0], event.pos[1]]):
            pygame.draw.rect(self.image, [255, 255, 255], (0, 0, 8, 8), 1)
            self.callback(self)
        else:
            self.image.fill(self.color)
