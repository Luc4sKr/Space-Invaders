import pygame
import sys

from player import Player

class Game:
    def __init__(self):
        player_sprite = Player((SCREEN_X / 2, SCREEN_Y), SCREEN_X, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)


    def run(self):
        # Atualizar todos os grupos de sprites
        # Desenhar todos os grupos de sprites
        self.player.update()

        self.player.sprite.laser_group.draw(screen)
        self.player.draw(screen)





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