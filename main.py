import pygame

from sys import exit
from random import choice, randint

from scripts import obstacle
from scripts.player import Player
from scripts.alien import Alien, Extra
from scripts.laser import Laser

from utils.util import Data


class Menu:
    def __init__(self):
        # Click do mouse
        self.click = False

        # Controle dos laços de repetição
        self.show_menu = True
        self.show_help_screen = False
        self.show_highscores_screen = False

        # Classe para estilizar o jogo
        self.crt = CRT()

    def menu(self):
        self.show_menu = True
        self.click = False
        while self.show_menu:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.show_menu = False
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            draw_text("SPACE", 42, (255, 255, 255), SCREEN_X/2, 80)
            draw_text("INVADERS", 42, (255, 255, 255), SCREEN_X/2, 120)
            draw_text("in python", 18, (55,113,161), SCREEN_X/2, 150)

            new_game_button = self.create_button(SCREEN_X/2 - 120, 220, SCREEN_X/2 - 50, 50, (0, 0, 0), "NEW GAME")
            highscores_button = self.create_button(SCREEN_X/2 - 120, 280, SCREEN_X/2 - 50, 50, (0, 0, 0), "HIGHTSCORES")
            help_button = self.create_button(SCREEN_X/2 - 120, 340, SCREEN_X/2 - 50, 50, (0, 0, 0), "HELP")
            quit_button = self.create_button(SCREEN_X/2 - 120, 400, SCREEN_X/2 - 50, 50, (0, 0, 0), "QUIT")

            mx, my = pygame.mouse.get_pos()
            if new_game_button.collidepoint((mx, my)):
                if self.click:
                    self.show_menu = False
                    new_game()
            if highscores_button.collidepoint((mx, my)):
                if self.click:
                    self.highscores_screen()
            if help_button.collidepoint((mx , my)):
                if self.click:
                    self.help_screen()
            if quit_button.collidepoint((mx, my)):
                if self.click:
                    pygame.quit()
                    exit()

            self.click = False

            self.crt.draw()
            pygame.display.update()
            screen.fill((0, 0, 0))

    def help_screen(self):
        self.show_help_screen = True
        self.click = False
        while self.show_help_screen:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            draw_text("HELP", 42, (255, 255, 255), SCREEN_X/2, 80)

            draw_text("COMANDS", 22, (255, 255, 255), 100, 150)

            draw_text("- MOVIMENTATION", 14, (255, 255, 255), 50, 170, topleft=True)
            menu.create_button(50, 200, 50, 50, (0, 0, 0), "<-")
            menu.create_button(120, 200, 50, 50, (0, 0, 0), "->")
            draw_text("OR", 18, (255, 255, 255), 250, 220)
            menu.create_button(330, 200, 50, 50, (0, 0, 0), "A")
            menu.create_button(400, 200, 50, 50, (0, 0, 0), "D")

            draw_text("- SHOOT", 14, (255, 255, 255), 50, 270, topleft=True)
            menu.create_button(50, 300, 250, 50, (0, 0, 0), "SPACE")

            draw_text("- PAUSE", 14, (255, 255, 255), 50, 370,topleft=True)
            menu.create_button(50, 400, 50, 50, (0, 0, 0), "ESC")


            back_to_menu_button = menu.create_button(150, 530, 300, 50, (0, 0, 0), "BACK TO MENU")

            mx, my = pygame.mouse.get_pos()
            if back_to_menu_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    self.show_help_screen = False

            self.click = False

            self.crt.draw()
            pygame.display.update()
            screen.fill((0, 0, 0))

    def highscores_screen(self):
        self.show_highscores_screen = True
        self.click = False
        while self.show_highscores_screen:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            draw_text("HIGHSCORES", 42, (255, 255, 255), SCREEN_X/2, 80)

            y_pos = 0
            for v in data.json_obj["score"]:
                draw_text(f"Score: {v}", 16, (255, 255, 255), SCREEN_X/8 - 30, 150 + y_pos, topleft=True)
                y_pos += 20

            y_pos = 0
            for v in data.json_obj["date"]:
                draw_text(f"Date: {v}", 16, (255, 255, 255), SCREEN_X/2 , 150 + y_pos, topleft=True)
                y_pos += 20

            back_to_menu_button = menu.create_button(150, 530, 300, 50, (0, 0, 0), "BACK TO MENU")
            reset_button = menu.create_button(500, 550, 80, 30, (0, 0, 0), "RESET", font_size=12)

            mx, my = pygame.mouse.get_pos()
            if back_to_menu_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    self.show_highscores_screen = False

            if reset_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    data.reset()

            self.click = False

            self.crt.draw()
            pygame.display.update()
            screen.fill((0, 0, 0))

    @staticmethod
    def create_button(x1, y1, x2, y2, color, text, font_size=18):
        button_border = pygame.Rect(x1 - 2, y1 - 2, x2 + 4, y2 + 4)
        button = pygame.Rect(x1, y1, x2, y2)
        pygame.draw.rect(screen, (255, 255, 255), button_border)
        pygame.draw.rect(screen, color, button)
        draw_text(text, font_size, (255, 255, 255), x1+(x2/2), y1+(y2/2))
        return button


class Game:
    def __init__(self):
        self.game_over = False

        self.crt = CRT()

        # Player
        player_sprite = Player((SCREEN_X / 2, SCREEN_Y), SCREEN_X, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Health
        self.lives = 3
        self.lives_surface = pygame.image.load("assets/images/player.png").convert_alpha()
        self.lives_x_start_pos = SCREEN_X - (self.lives_surface.get_size()[0] * 3  + 30)

        # Score
        self.score = 0
        self.font = pygame.font.Font("assets/8-bit_font.ttf", 20)

        # Obstacle
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks_group = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_positions = [num * (SCREEN_X / self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.create_multiple_obstacles(*self.obstacle_x_positions, x_start=SCREEN_X/15, y_start=480) # Não sei pq 15 :)

        # Alien
        self.alien_group = pygame.sprite.Group()
        self.alien_setup(rows=6, cols=8, x_distance=60, y_distance=48, x_offet=70, y_offset=100)
        self.alien_direction = 1
        self.alien_lasers_group = pygame.sprite.Group()

        # Extra alien
        self.extra_alien = pygame.sprite.GroupSingle()
        self.extra_spawn_time = randint(400, 800)

        # Audio
        self.music = pygame.mixer.Sound("assets/audio/music.wav")
        self.music.set_volume(0.06)
        self.music.play(loops=-1)

        self.laser_sound = pygame.mixer.Sound("assets/audio/laser.wav")
        self.laser_sound.set_volume(0.08)

        self.explosion_sound = pygame.mixer.Sound("assets/audio/explosion.wav")
        self.explosion_sound.set_volume(0.1)

        # Mouse
        self.click = False

    def create_obstacle(self, x_start, y_start, off_set_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == "1":
                    x = x_start + col_index * self.block_size + off_set_x
                    y = y_start + row_index * self.block_size
                    block = obstacle.Block(self.block_size, (240, 80, 80), x, y)
                    self.blocks_group.add(block)

    def create_multiple_obstacles(self, *offset, x_start, y_start):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)

    def alien_setup(self, rows, cols, x_distance, y_distance, x_offet, y_offset):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offet
                y = row_index * y_distance + y_offset

                if row_index == 0:
                    alien_sprite = Alien("yellow", x, y)
                elif 1 <= row_index <= 2:
                    alien_sprite = Alien("green", x, y)
                else:
                    alien_sprite = Alien("red", x, y)

                self.alien_group.add(alien_sprite)

    def alien_position_checker(self):
        all_aliens = self.alien_group.sprites()
        for aliens in all_aliens:
            if aliens.rect.right >= SCREEN_X:
                self.alien_direction = -1
                self.alien_move_down(2)
            if aliens.rect.left <= 0:
                self.alien_direction = 1
                self.alien_move_down(2)

    def alien_move_down(self, distance):
        if self.alien_group:
            for alien in self.alien_group.sprites():
                alien.rect.y += distance

    def alien_shot(self):
        if self.alien_group.sprites():
            random_alien = choice(self.alien_group.sprites())
            laser_sprite = Laser(random_alien.rect.center, 6)
            self.alien_lasers_group.add(laser_sprite)
            self.laser_sound.play() # Som do laser

    def extra_alien_timer(self):
        self.extra_spawn_time -= 1
        if self.extra_spawn_time <= 0:
            self.extra_alien.add(Extra(choice(["right", "left"])))
            self.extra_spawn_time = randint(400, 800)

    def collision_checks(self):
        # Player lasers
        if self.player.sprite.laser_group:
            for laser in self.player.sprite.laser_group:
                # Obstacle collisions
                if pygame.sprite.spritecollide(laser, self.blocks_group, True):
                    laser.kill()

                # Alien collisions
                alien_hit = pygame.sprite.spritecollide(laser, self.alien_group, True)
                if alien_hit:
                    for alien in alien_hit:
                        self.score += alien.value
                    laser.kill()
                    self.explosion_sound.play() # Som do explossão com o alien

                # Extra alien collision
                if pygame.sprite.spritecollide(laser, self.extra_alien, True):
                    laser.kill()
                    self.score += 500

        # Alien lasers
        if self.alien_lasers_group:
            for laser in self.alien_lasers_group:
                # Obstacle collisions
                if pygame.sprite.spritecollide(laser, self.blocks_group, True):
                    laser.kill()

                # Player collision
                if pygame.sprite.spritecollide(laser, self.player, False):
                    laser.kill()
                    self.lives -= 1

        # Aliens
        if self.alien_group:
            for alien in self.alien_group:
                pygame.sprite.spritecollide(alien, self.blocks_group, True)

                if pygame.sprite.spritecollide(alien, self.player, False):
                    pygame.quit()
                    exit()

    def display_lives(self):
        for live in range(self.lives):
            x = self.lives_x_start_pos + (live * (self.lives_surface.get_size()[0] + 10))
            screen.blit(self.lives_surface, (x, 8))

    def display_score(self):
        draw_text(f"SCORE: {self.score}", 16, (255, 255, 255), 20, 30, topleft=True)

    def victory_screen(self):
        if not self.alien_group.sprites():
            draw_text("YOU WON", 44, (0, 255, 0), SCREEN_X/2, 200)

            back_to_menu_button = menu.create_button(150, 250, 400 - 100, 50, (0, 0, 0), "BACK TO MENU")

            mx, my = pygame.mouse.get_pos()
            if back_to_menu_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    self.game_over = True
                    self.music.stop()
                    data.add_score(self.score)
                    menu.menu()

    def game_over_screen(self):
        if self.lives <= 0:
            draw_text("YOU LOSE", 44, (255, 0, 0), SCREEN_X/2, 200)
            back_to_menu_button = menu.create_button(150, 250, 300, 50, (0, 0, 0), "BACK TO MENU")

            mx, my = pygame.mouse.get_pos()
            if back_to_menu_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    self.game_over = True
                    self.music.stop()
                    data.add_score(self.score)
                    menu.menu()

    def pause_menu_screen(self):
        self.show_pause_menu_screen = True
        self.click = False
        while self.show_pause_menu_screen:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            draw_text("PAUSE", 42, (255, 255, 255), SCREEN_X/2, 80)

            back_to_game_button = menu.create_button(150, 170, 300, 50, (0, 0, 0), "BACK TO GAME")
            back_to_menu_button = menu.create_button(150, 230, 300, 50, (0, 0, 0), "BACK TO MENU")
            quit_button = menu.create_button(150, 290, 300, 50, (0, 0, 0), "QUIT GAME")

            mx, my = pygame.mouse.get_pos()
            if back_to_game_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    self.show_pause_menu_screen = False
            if back_to_menu_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    self.show_pause_menu_screen = False
                    self.game_over = True
                    self.music.stop()
                    menu.menu()
            if quit_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    pygame.quit()
                    exit()

            self.click = False

            self.crt.draw()
            pygame.display.update()
            screen.fill((0, 0, 0))

    def run(self):
        # Atualiza todos os grupos de sprites
        self.alien_position_checker()
        self.collision_checks()
        if self.alien_group.sprites():
            self.extra_alien_timer()

        self.display_lives()
        self.display_score()

        # Para quando as vidas acabarem, tudo fica parado
        if self.lives > 0:
            self.player.update()
            self.alien_lasers_group.update()
            self.extra_alien.update()
            self.alien_group.update(self.alien_direction)

        # Desenha todos os grupos de sprites
        self.player.sprite.laser_group.draw(screen)
        self.player.draw(screen)

        self.blocks_group.draw(screen)
        self.alien_group.draw(screen)
        self.alien_lasers_group.draw(screen)
        self.extra_alien.draw(screen)

        # Telas
        self.game_over_screen()
        self.victory_screen()

        self.click = False


class CRT:
    def __init__(self):
        self.tv = pygame.image.load("assets/images/tv.png").convert_alpha()
        self.tv = pygame.transform.scale(self.tv, (SCREEN_X, SCREEN_Y))

    def draw(self):
        self.tv.set_alpha(randint(75, 90))
        self.create_crt_lines()

        screen.blit(self.tv, (0, 0))

    def create_crt_lines(self):
        line_height = 3
        line_amount = int(SCREEN_X / line_height)
        for line in range(line_amount):
            y_pos = line * line_height
            pygame.draw.line(self.tv, "black", (0, y_pos), (SCREEN_X, y_pos), 1)


if __name__ == '__main__':
    pygame.init()

    SCREEN_X = 600
    SCREEN_Y = 600

    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()
    FPS = 60

    def draw_text(text, tam, color, x, y, topleft=False):
        fonte = pygame.font.Font("assets/8-bit_font.ttf", tam)
        text_obj = fonte.render(text, False, color)
        text_rect = text_obj.get_rect()
        if topleft:
            text_rect.topleft = (x, y)
        else:
            text_rect.center = (x, y)
        screen.blit(text_obj, text_rect)

    def new_game():
        game = Game()
        crt = CRT()

        ALIENLASER = pygame.USEREVENT + 1
        pygame.time.set_timer(ALIENLASER, 800)
        while not game.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == ALIENLASER:
                    if game.lives > 0:
                        game.alien_shot()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        game.click = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game.pause_menu_screen()

            screen.fill((0, 0, 0))

            game.run()
            crt.draw()

            pygame.display.flip()
            clock.tick(60)


    data = Data()
    menu = Menu()

    menu.menu()