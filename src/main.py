import os
print(f"Current Working Directory: {os.getcwd()}")

os.environ["API_KEY"] = "AIzaSyASIPdX9_sJeVJ_Hzzhvzi3082qIE0VcKo"

print(f"API_KEY is: {os.environ.get('API_KEY')}")

import pygame
from src.settings import WIDTH, HEIGHT

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My GenAI Game")

clock = pygame.time.Clock()

from src.game import update_game, draw_game

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    update_game()
    draw_game(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()



