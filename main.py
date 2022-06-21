import pygame

from sys import exit
from random import choice, randint
from os import path, getcwd

from scripts import obstacle
from scripts.player import Player
from scripts.alien import Alien, Extra
from scripts.laser import Laser

from utils.util import Data


class Menu:
    """
    Classe responsável pelo menu principal do jogo
    """
    def __init__(self):
        # Click do mouse
        self.click = False

        # Controle dos laços de repetição
        self.show_menu = True
        self.show_help_screen = False
        self.show_highscores_screen = False

    def menu(self):
        """
        Menu principal do jogo
        """
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

            # Título do jogo
            draw_text("SPACE", 42, (255, 255, 255), SCREEN_X/2, 80)
            draw_text("INVADERS", 42, (255, 255, 255), SCREEN_X/2, 120)
            draw_text("in python", 18, (55,113,161), SCREEN_X/2, 150)

            # Botões do menu
            new_game_button = self.create_button(SCREEN_X/2 - 120, 220, SCREEN_X/2 - 50, 50, (0, 0, 0), "NEW GAME")
            highscores_button = self.create_button(SCREEN_X/2 - 120, 280, SCREEN_X/2 - 50, 50, (0, 0, 0), "HIGHTSCORES")
            help_button = self.create_button(SCREEN_X/2 - 120, 340, SCREEN_X/2 - 50, 50, (0, 0, 0), "HELP")
            quit_button = self.create_button(SCREEN_X/2 - 120, 400, SCREEN_X/2 - 50, 50, (0, 0, 0), "QUIT")

            # Posição do mouse
            mx, my = pygame.mouse.get_pos()

            # Checa o input com os botões do menu
            if new_game_button.collidepoint((mx, my)):
                if self.click:
                    self.show_menu = False
                    new_game()
            if highscores_button.collidepoint((mx, my)):
                if self.click:
                    data.organize_file()
                    self.highscores_screen()
            if help_button.collidepoint((mx , my)):
                if self.click:
                    self.help_screen()
            if quit_button.collidepoint((mx, my)):
                if self.click:
                    pygame.quit()
                    exit()

            # Depois de checar os inputs o click fica falso
            self.click = False

            # Style/Update
            crt.draw()
            pygame.display.update()
            screen.fill((0, 0, 0))

    def help_screen(self):
        """
        Tela de ajuda (mostra os comandos para jogar o jogo)
        """
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

            # Texto e botões
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

            # Posição do mouse
            mx, my = pygame.mouse.get_pos()

            # Checa o input com os botões do menu
            if back_to_menu_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    self.show_help_screen = False

            # Depois de checar os inputs o click fica falso
            self.click = False

            # Style/Update
            crt.draw()
            pygame.display.update()
            screen.fill((0, 0, 0))

    def highscores_screen(self):
        """
        Tela de score (mostra os maiores scores)
        """
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

            # Título
            draw_text("HIGHSCORES", 42, (255, 255, 255), SCREEN_X/2, 80)

            # Laço para desenhar toda a lista de scores
            y_pos = 0
            for v in data.json_obj["score"]:
                draw_text(f"Score: {v}", 16, (255, 255, 255), SCREEN_X/8 - 30, 150 + y_pos, topleft=True)
                y_pos += 20

            # Laço pra desenhar toda a lista de datas
            y_pos = 0
            for v in data.json_obj["date"]:
                draw_text(f"Date: {v}", 16, (255, 255, 255), SCREEN_X/2 , 150 + y_pos, topleft=True)
                y_pos += 20

            # Botões
            back_to_menu_button = menu.create_button(150, 530, 300, 50, (0, 0, 0), "BACK TO MENU")
            reset_button = menu.create_button(500, 550, 80, 30, (0, 0, 0), "RESET", font_size=12) # Botão que reseta a lista de scores

            # Posição do mouse
            mx, my = pygame.mouse.get_pos()

            # Checa o input com os botões do menu
            if back_to_menu_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    self.show_highscores_screen = False
            if reset_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    data.reset()

            # Depois de checar os inputs o click fica falso
            self.click = False

            # Style/Update
            crt.draw()
            pygame.display.update()
            screen.fill((0, 0, 0))

    @staticmethod
    def create_button(left, top, width, height, color, text, font_size=18):
        """
        Função para criar botões
        :param left: Posição x da parte esquerda do botão.
        :param top: Posição y do topo do botão.
        :param width: Largura do botão.
        :param height: Altura do botão.
        :param color: Cor do botão.
        :param text: Texto que vai dentro do botão.
        :param font_size: Tamanho da fonte do botão.
        :return: Retorna o botão para ser utilizado para checar inputs do mouse.
        """
        button_border = pygame.Rect(left - 2, top - 2, width + 4, height + 4)
        button = pygame.Rect(left, top, width, height)
        pygame.draw.rect(screen, (255, 255, 255), button_border)
        pygame.draw.rect(screen, color, button)
        draw_text(text, font_size, (255, 255, 255), left+(width/2), top+(height/2))
        return button


class Game:
    """
    Classe responsável por toda a lógica do jogo
    """
    def __init__(self, score=0):
        # Controle dos laços de repetição
        self.game_over = False
        self.show_pause_menu_screen = False

        # Classe para estilizar o jogo
        self.crt = CRT()

        # Player
        player_sprite = Player((SCREEN_X / 2, SCREEN_Y), SCREEN_X, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Vida
        self.lives = 3
        self.lives_surface = pygame.image.load(path.join(getcwd() + "/assets/images/player.png")).convert_alpha()
        self.lives_x_start_pos = SCREEN_X - (self.lives_surface.get_size()[0] * 3  + 30)

        # Score
        self.score = score

        # Obstáculo
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
        self.extra_alien = pygame.sprite.GroupSingle(None)
        self.extra_spawn_time = randint(400, 800)

        # Música
        self.music = pygame.mixer.Sound("assets/audio/music.wav")
        self.music.set_volume(0.06)
        self.music.play(loops=-1)

        # Som do laser
        self.laser_sound = pygame.mixer.Sound("assets/audio/laser.wav")
        self.laser_sound.set_volume(0.08)

        # Som da explosão
        self.explosion_sound = pygame.mixer.Sound("assets/audio/explosion.wav")
        self.explosion_sound.set_volume(0.1)

        # Mouse
        self.click = False

    def create_obstacle(self, x_start, y_start, off_set_x):
        """
        Cria um obstáculo. A lista da classe dos obstáculos é formada por '0' e '1', que formam a figura do obstáculo,
        se na coluna tiver um '1' ele cria um bloco, e os blocos formam o obstáculo.
        :param x_start: Posição inicial do eixo x.
        :param y_start: Posição inicial do eixo y.
        :param off_set_x: Deslocamento do eixo x (para dar um espaço entre os obstáculos).
        """
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == "1":
                    x = x_start + col_index * self.block_size + off_set_x
                    y = y_start + row_index * self.block_size
                    block = obstacle.Block(self.block_size, (240, 80, 80), x, y)
                    self.blocks_group.add(block)

    def create_multiple_obstacles(self, *offset, x_start, y_start):
        """
        Cria vários obstáculos.
        :param offset: Deslocamento
        :param x_start: Posição inicial do eixo x.
        :param y_start: Posição inicial do eixo y.
        """
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)

    def alien_setup(self, rows, cols, x_distance, y_distance, x_offet, y_offset):
        """
        Configuração dos aliens.
        :param rows: Número de linhas.
        :param cols: Número de colunas.
        :param x_distance: Distancia do eixo x.
        :param y_distance: Distancia do eixo y.
        :param x_offet: Deslocamento do eixo x.
        :param y_offset: Deslocamento do eixo y.
        """
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
        """
        Verifica se os aliens colidiram com a lateral da tela ou se colidiram com a borda inferior.
        Se colidir com a borda inferior o Player perde.
        Se colidir com as laterais o Alien se move para baixo.
        """
        all_aliens = self.alien_group.sprites()
        for aliens in all_aliens:
            if aliens.rect.right >= SCREEN_X:
                self.alien_direction = -1
                self.alien_move_down(2)
            if aliens.rect.left <= 0:
                self.alien_direction = 1
                self.alien_move_down(2)
            if aliens.rect.bottom >= SCREEN_Y:
                self.lives = 0

    def alien_move_down(self, distance):
        """
        Movimenta os aliens para baixo
        :param distance: Distancia de movimentação do alien
        """
        if self.alien_group:
            for alien in self.alien_group.sprites():
                alien.rect.y += distance

    def alien_shot(self):
        """
        Um alien aleatório atira um laser.
        """
        if self.alien_group.sprites():
            random_alien = choice(self.alien_group.sprites())
            laser_sprite = Laser(random_alien.rect.center, 6)
            self.alien_lasers_group.add(laser_sprite)
            self.laser_sound.play()

    def extra_alien_timer(self):
        """
        Cronômetro de aparição do alien extra.
        """
        self.extra_spawn_time -= 1
        if self.extra_spawn_time <= 0:
            self.extra_alien.add(Extra(choice(["right", "left"])))
            self.extra_spawn_time = randint(400, 800)

    def collision_checks(self):
        """
        Checagem das colisões do jogo.
        """
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
                    self.lives -= 1

    def display_lives(self):
        """
        Desenha as vidas do Player na tela.
        """
        for live in range(self.lives):
            x = self.lives_x_start_pos + (live * (self.lives_surface.get_size()[0] + 10))
            screen.blit(self.lives_surface, (x, 8))

    def display_score(self):
        """
        Desenha o score na tela.
        """
        draw_text(f"SCORE: {self.score}", 16, (255, 255, 255), 20, 30, topleft=True)

    def victory_screen(self):
        """
        Mostra a tela de vitória quando o Player mata todos os Aliens.
        """
        if not self.alien_group.sprites():
            draw_text("YOU WON", 44, (0, 255, 0), SCREEN_X/2, 200)

            back_to_menu_button = menu.create_button(150, 250, 300, 50, (0, 0, 0), "BACK TO MENU")
            continue_game_button = menu.create_button(150, 310, 300, 50, (0, 0, 0), "CONTINUE GAME")

            mx, my = pygame.mouse.get_pos()

            if back_to_menu_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    self.game_over = True
                    self.music.stop()
                    data.add_score(self.score)
                    menu.menu()
            if continue_game_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    self.game_over = True
                    self.music.stop()
                    new_game(score=self.score)

    def game_over_screen(self):
        """
        Mostra a tela de derrota quando player morre, ou quando o Alien colide com o Player.
        """
        if self.lives <= 0:
            draw_text("YOU LOSE", 44, (255, 0, 0), SCREEN_X/2, 200)

            back_to_menu_button = menu.create_button(150, 250, 300, 50, (0, 0, 0), "BACK TO MENU")
            new_game_button = menu.create_button(150, 310, 300, 50, (0, 0, 0), "NEW GAME")

            mx, my = pygame.mouse.get_pos()

            if back_to_menu_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    self.game_over = True
                    self.music.stop()
                    data.add_score(self.score)
                    menu.menu()
            if new_game_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    self.game_over = True
                    self.music.stop()
                    data.add_score(self.score)
                    new_game()

    def pause_menu_screen(self):
        """
        Tela de pause
        """
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
        """
        Função que faz o jogo rodar, atualiza, checa colisões, desenha na tela, etc...
        """

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

        # No final de tudo o click do mouse volta a ser falso
        self.click = False


class CRT:
    """
    Classe para deixar o estilo do jogo um pouco mais retrô
    """
    def __init__(self):
        # Bordas de TV antiga
        self.tv = pygame.image.load(path.join(getcwd() + "/assets/images/tv.png")).convert_alpha()
        self.tv = pygame.transform.scale(self.tv, (SCREEN_X, SCREEN_Y))

    def draw(self):
        """
        Desenha na tela
        """
        self.tv.set_alpha(randint(75, 90))
        self.create_crt_lines()

        screen.blit(self.tv, (0, 0))

    def create_crt_lines(self):
        """
        Cria linhas para dar um estilo retrô para o jogo
        """
        line_height = 3
        line_amount = int(SCREEN_X / line_height)
        for line in range(line_amount):
            y_pos = line * line_height
            pygame.draw.line(self.tv, "black", (0, y_pos), (SCREEN_X, y_pos), 1)


if __name__ == '__main__':
    # Inicia o pygame
    pygame.init()

    # Tamanho da tela
    SCREEN_X = 600
    SCREEN_Y = 600

    # Tela
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    pygame.display.set_caption("Space Invaders") # Nome do jogo que fica na janela do jogo

    # Ajuda a controlar a taxa de atualização do jogo - FPS
    clock = pygame.time.Clock()
    FPS = 60

    def draw_text(text, tam, color, x, y, topleft=False):
        """
        Desenha um texto na tela
        :param text: Texto.
        :param tam: Tamanho do texto.
        :param color: Cor do texto.
        :param x: Posição do eixo x.
        :param y: Posição do eixo y.
        :param topleft: Se o parametro for True se baseia no topo esquerdo para as cordenadas.
        """
        fonte = pygame.font.Font("assets/8-bit_font.ttf", tam)
        text_obj = fonte.render(text, False, color)
        text_rect = text_obj.get_rect()
        if topleft:
            text_rect.topleft = (x, y)
        else:
            text_rect.center = (x, y)
        screen.blit(text_obj, text_rect)

    def new_game(score=0):
        """
        Cria um novo jogo.
        """
        game = Game(score)

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


    # Classe dos dados do jogo
    data = Data()

    # Classe para estilizar o jogo
    crt = CRT()

    # Classe do menu
    menu = Menu()


    # --- COMEÇA O JOGO AQUI --- #
    menu.menu() # Começa o jogo pelo menu