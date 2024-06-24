# 2. Создать движение фотографии

import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Движение картинки")

image = pygame.image.load("arrow.png")
image = pygame.transform.scale(image, (200, 100))
airplane_rect = image.get_rect()

x, y = width // 2, height // 2
speed = 5
angle = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        y -= speed
        angle = 90  # Повернуть стрелку вверх
    if keys[pygame.K_s]:
        y += speed
        angle = 270  # Повернуть стрелку вниз
    if keys[pygame.K_a]:
        x -= speed
        angle = 180  # Повернуть стрелку влево
    if keys[pygame.K_d]:
        x += speed
        angle = 0  # Повернуть стрелку вправо

    rotated_airplane = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_airplane.get_rect(center=(x, y))

    screen.fill(WHITE)  # Устанавливаем белый фон
    screen.blit(rotated_airplane, rotated_rect.topleft)

    pygame.display.flip()
    clock.tick(30)
