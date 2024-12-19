import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Игра ТИР')
target_icon = pygame.image.load("images/target2.png")
pygame.display.set_icon(target_icon)


target_image = pygame.image.load("images/target_corrected.jpeg")
TARGET_WIDTH = 80
TARGET_HEIGHT = 80
target_x = random.randint(0, SCREEN_WIDTH - TARGET_WIDTH)
target_y = random.randint(0, SCREEN_HEIGHT - TARGET_HEIGHT)

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + TARGET_WIDTH and target_y <= mouse_y <= target_y + TARGET_HEIGHT:
                target_x = random.randint(0, SCREEN_WIDTH - TARGET_WIDTH)
                target_y = random.randint(0, SCREEN_HEIGHT - TARGET_HEIGHT)

    screen.blit(target_image, (target_x, target_y))
    pygame.display.update()

pygame.quit()