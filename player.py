import pygame

from laser import Laser

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, constraint, speed):
        super().__init__()

        self.image = pygame.image.load("assets/images/player.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = speed
        self.max_x_constraint = constraint
        self.ready = True
        self.laser_time = 0 # get_ticks
        self.laser_cooldown = 600

        self.laser_group = pygame.sprite.Group()

        self.laser_sound = pygame.mixer.Sound("assets/audio/laser.wav")
        self.laser_sound.set_volume(0.08)

    def get_input(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.rect.x += self.speed
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.rect.x -= self.speed

        if key[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()
            self.laser_sound.play()

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True

    def shoot_laser(self):
        self.laser_group.add(Laser(self.rect.center, -8))

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint

    def update(self):
        self.get_input()
        self.constraint()
        self.recharge()
        self.laser_group.update()