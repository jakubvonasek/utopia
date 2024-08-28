import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, description):
        super().__init__()
        self.description = description
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Temporary visual
        self.rect = self.image.get_rect()
        # Additional attributes can be set based on the description
        self.speed = 5  # Example attribute

    def update(self):
        self.rect.x += self.speed
