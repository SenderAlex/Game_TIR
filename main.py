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

target_image2 = pygame.Surface((TARGET_WIDTH, TARGET_HEIGHT), pygame.SRCALPHA)


target_x = random.randint(0, SCREEN_WIDTH - TARGET_WIDTH)
target_y = random.randint(0, SCREEN_HEIGHT - TARGET_HEIGHT)

radiuss = [4, 9, 17, 25, 33, 40]
points = 0
target = 0

center_x = TARGET_WIDTH // 2
center_y = TARGET_HEIGHT // 2

running = True
while running:
    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            relative_x = mouse_x - target_x
            relative_y = mouse_y - target_y

            if 0 <= relative_x <= TARGET_WIDTH and 0 <= relative_y <= TARGET_HEIGHT:
                for i, radius in enumerate(radiuss):
                    distance = ((relative_x - center_x)**2 + (relative_y - center_y)**2)**0.5
                    if distance <= radius:
                        points += (10 - i)
                        target = 10 - i
                        break
                target_x = random.randint(0, SCREEN_WIDTH - TARGET_WIDTH)
                target_y = random.randint(0, SCREEN_HEIGHT - TARGET_HEIGHT)

    target_image2.fill((0, 0, 0, 0))
    for radius in radiuss:
        pygame.draw.circle(target_image2, (0, 0, 0), (center_x, center_y), radius, 1)

    screen.blit(target_image, (target_x, target_y))
    #screen.blit(target_image2, (target_x, target_y))

    font = pygame.font.Font(None, 30)
    score = font.render(f'Количество набранных очков {points}', True, (0, 255, 0))
    screen.blit(score, (250, 5))

    font = pygame.font.Font(None, 30)
    target_score = font.render(f'    Вы попали в "{target}"', True, (0, 255, 0))
    screen.blit(target_score, (305, 25))

    pygame.display.update()

pygame.quit()