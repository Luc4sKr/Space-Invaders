import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed):
        super().__init__()

        self.image = pygame.Surface((4, 20))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = speed

    def destroy_laser(self):
        if self.rect.bottom  <= 0 or self.rect.top > 600:
            self.kill()

    def update(self):
        self.rect.y += self.speed

        self.destroy_laser()