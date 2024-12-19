import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Игра ТИР')

target_image = pygame.image.load("images/target.jpeg")
TARGET_WIDTH = 80
TARGET_HEIGHT = 60
target_x = random.randint(0, SCREEN_WIDTH - TARGET_WIDTH)
target_y = random.randint(0, SCREEN_HEIGHT - TARGET_HEIGHT)

running = True
while running:
    screen.fill(color)



pygame.quit()