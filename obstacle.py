import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, size, color, x, y):
        super().__init__()

        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x,y))


shape = [
    "00111111100",
    "01111111110",
    "11111111111",
    "11111111111",
    "11111111111",
    "11100000111",
    "11000000011"
]