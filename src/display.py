import pygame
import map
from tiles import grass, water


# TODO: Multiple select


class Display(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        self.size = self.width, self.height = size
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.image.fill([255, 0, 255])
        self.map_data = map.Map('../assets/maps/map.dat', size).get_map()
        self.sprite_map = pygame.sprite.Group()
        self.selected = []
        self.draw_map()

    def set_selected(self, sprite):
        self.selected = [sprite]

    def draw_map(self):
        for y, _ in enumerate(self.map_data):
            for x, _ in enumerate(self.map_data[0]):
                if self.map_data[y][x] == 0:
                    self.sprite_map.add(grass.Grass([x*8, y*8], callback=self.set_selected))
                else:
                    self.sprite_map.add(water.Water([x*8, y*8], callback=self.set_selected))

    def get_image(self, display_size):
        return pygame.transform.scale(self.image, display_size)

    def update(self, event):
        self.sprite_map.update(event)

    def render(self):
        self.sprite_map.draw(self.image)
        self.image.blit(pygame.font.Font('../assets/fonts/Px437_AMI_EGA_8x8.ttf', 8).render(
            str(self.selected), False, [255, 255, 255]
        ), [0, self.height - 8])
