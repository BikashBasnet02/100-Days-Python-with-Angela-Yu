import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
FROG_COLOR = (0, 255, 0)
CAR_COLOR = (255, 0, 0)
LOG_COLOR = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Frogger")
clock = pygame.time.Clock()

class Frog(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(FROG_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((50, 30))
        self.image.fill(CAR_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH

class Log(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((100, 30))
        self.image.fill(LOG_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH

all_sprites = pygame.sprite.Group()
cars = pygame.sprite.Group()
logs = pygame.sprite.Group()

frog = Frog()
all_sprites.add(frog)

for _ in range(5):
    x = random.randrange(0, SCREEN_WIDTH)
    y = random.randrange(100, 300)
    speed = random.choice([-3, 3])
    car = Car(x, y, speed)
    all_sprites.add(car)
    cars.add(car)

for _ in range(5):
    x = random.randrange(0, SCREEN_WIDTH)
    y = random.randrange(350, 500)
    speed = random.choice([-2, 2])
    log = Log(x, y, speed)
    all_sprites.add(log)
    logs.add(log)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    frog_hit_cars = pygame.sprite.spritecollide(frog, cars, False)
    if frog_hit_cars:
        frog.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)

    frog_on_logs = pygame.sprite.spritecollide(frog, logs, False)
    if frog_on_logs:
        frog.rect.x += frog_on_logs[0].speed

    screen.fill(BACKGROUND_COLOR)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
