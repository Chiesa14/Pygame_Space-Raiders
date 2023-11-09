import time
import pygame
import serial
import random

pygame.init()

arduinoData = serial.Serial("/dev/ttyACM0", 9600)

HEIGHT = 700
WIDTH = 1000

# fonts
font = pygame.font.Font('assets/Space Game.ttf', 40)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

pygame.display.set_caption("Space Raiders")

character_image = pygame.image.load('assets/pixel_ship_yellow.png')
bg = pygame.image.load('assets/background-black.png')
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

# Sounds
bg_sound = pygame.mixer.music.load('assets/bg.mp3')
pygame.mixer.music.set_volume(.2)
pygame.mixer.music.play(-1)
shooting_sound = pygame.mixer.Sound('shoot.wav')


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    lives = 3

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/pixel_ship_green_small.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = 3

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()


character = character_image.get_rect()
character_x = (WIDTH - character.width) // 2
character_y = (HEIGHT - character.height) - 10

move_speed = 5

bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()

last_shot_time = time.time()
cooldown_time = 0.35

enemy_spawn_delay = 1.0
last_enemy_spawn_time = time.time() - enemy_spawn_delay
max_enemies_on_screen = 5

score = 0
lives = 3

restart_button = pygame.Rect(300, 250, 150, 50)
quit_button = pygame.Rect(300, 350, 150, 50)

run = True


def shoot():
    global last_shot_time
    current_time = time.time()
    if current_time - last_shot_time >= cooldown_time:
        bullet = Bullet(character_x + character.width // 2, character_y)
        bullets.add(bullet)
        shooting_sound.play()
        last_shot_time = current_time


def create_enemy():
    enemy = Enemy()
    enemies.add(enemy)


gameover = False


def game_over():
    global gameover
    pygame.mixer.music.stop()
    shooting_sound.stop()
    gameover = True
    screen.fill(black)
    game_over_text = font.render("🥹 Game Over !!!", True, red)
    text_rect = game_over_text.get_rect()
    text_rect.center = (screen.get_width() / 2, screen.get_height() / 2)
    screen.blit(game_over_text, text_rect)

    restart_button_color = (0, 255, 0) if restart_button.collidepoint(pygame.mouse.get_pos()) else (0, 128, 0)
    pygame.draw.rect(screen, restart_button_color, restart_button)
    restart_text = font.render("RESTART", True, (255, 255, 255))
    restart_text_rect = restart_text.get_rect()
    restart_text_rect.center = restart_button.center
    screen.blit(restart_text, restart_text_rect)

    quit_button_color = (255, 0, 0) if quit_button.collidepoint(pygame.mouse.get_pos()) else (128, 0, 0)
    pygame.draw.rect(screen, quit_button_color, quit_button)
    quit_text = font.render("QUIT", True, (255, 255, 255))
    quit_text_rect = quit_text.get_rect()
    quit_text_rect.center = quit_button.center
    screen.blit(quit_text, quit_text_rect)


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if not gameover:
        if arduinoData.inWaiting:
            data = arduinoData.readline().decode().strip()
            try:
                joy_x, joy_y, gun = map(int, data.split(" "))
                if joy_x != joy_y:
                    character_x += (joy_x - 514) // 100 * move_speed
                if gun != 1:
                    shoot()
                current_time = time.time()
                if current_time - last_enemy_spawn_time >= enemy_spawn_delay and len(enemies) < max_enemies_on_screen:
                    create_enemy()
                    last_enemy_spawn_time = current_time
            except ValueError as e:
                print("Error decoding: " + data)

        character_x = max(0, min(WIDTH - character.width, character_x))
        character_y = max(0, min(HEIGHT - character.height, character_y))

        screen.blit(bg, (0, 0))

        bullets.update()
        bullets.draw(screen)

        enemies.update()
        enemies.draw(screen)
        bullet_enemy_collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
        for enemy in bullet_enemy_collisions.keys():
            score += 1
            enemies.remove(enemy)

    enemy_character_collide = pygame.sprite.groupcollide(enemies, pygame.sprite.Group(), True, True)

    for enemy in enemies:
        if enemy.rect.bottom > HEIGHT:
            if lives >= 0:
                lives -= 1
            enemies.remove(enemy)
    if lives <= 0:
        game_over()
    if event.type == pygame.MOUSEBUTTONDOWN and restart_button.collidepoint(pygame.mouse.get_pos()):
        restart_game()
    if event.type == pygame.MOUSEBUTTONDOWN and quit_button.collidepoint(pygame.mouse.get_pos()):
        pygame.quit()
        exit()

    score_text = font.render("Score: " + str(score), True, white)
    lives_text = font.render("Lives: " + str(lives), True, red)

    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (WIDTH - lives_text.get_width() - 10, 10))
    screen.blit(character_image, (character_x, character_y))

    pygame.display.update()
