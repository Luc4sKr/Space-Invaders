import pygame
import sys

import obstacle
from player import Player

class Game:
    def __init__(self):
        # Player
        player_sprite = Player((SCREEN_X / 2, SCREEN_Y), SCREEN_X, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Obstacle
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks_group = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_positions = [num * (SCREEN_X / self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.create_multiple_obstacles(*self.obstacle_x_positions, x_start=SCREEN_X/15, y_start=480) # Não sei pq 15 :)

    def create_obstacle(self, x_start, y_start, off_set_x):
        for row_index, row in enumerate(self.shape):
          for col_index, col in enumerate(row):
              if col == "x":
                  x = x_start + col_index * self.block_size + off_set_x
                  y = y_start + row_index * self.block_size
                  block = obstacle.Block(self.block_size, (240, 80, 80), x, y)
                  self.blocks_group.add(block)

    def create_multiple_obstacles(self, *offset, x_start, y_start):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)


    def run(self):
        # Atualizar todos os grupos de sprites
        # Desenhar todos os grupos de sprites
        self.player.update()

        self.player.sprite.laser_group.draw(screen)
        self.player.draw(screen)

        self.blocks_group.draw(screen)


if __name__ == '__main__':
    pygame.init()

    SCREEN_X = 600
    SCREEN_Y = 600

    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()

    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        game.run()

        pygame.display.flip()
        clock.tick(60)