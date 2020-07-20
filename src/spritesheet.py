import pygame


class Spritesheet:
    def __init__(self, path):
        self.sheet = pygame.image.load(path).convert()
        self.color_key = [255, 0, 255]

    def image_at(self, size, offset):
        rect = pygame.Rect(offset + size)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        image.set_colorkey(self.color_key, pygame.RLEACCEL)
        return image
