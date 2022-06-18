import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        
        file_path = f"assets/images/{color}.png"
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Score
        if color == "red":
            self.value = 100
        if color == "green":
            self.value = 200
        if color == "yellow":
            self.value = 300

    def update(self, direction):
        self.rect.x += direction


class Extra(pygame.sprite.Sprite):
    def __init__(self, side):
        super().__init__()

        self.image = pygame.image.load("assets/images/extra.png").convert_alpha()

        if side == "right":
            x = 600 + 50
            self.speed = -3
        else:
            x = -50
            self.speed = 3

        self.rect = self.image.get_rect()
        self.rect.topleft=(x, 80)

    def update(self):
        self.rect.x += self.speed