from src.enemy import Enemy
from gen_ai.enemy_generator import generate_enemy

enemy_name = generate_enemy()
enemy = Enemy(enemy_name)
enemies_group = pygame.sprite.Group(enemy)

def update_game():
    enemies_group.update()
    # Other game update logic

def draw_game(screen):
    enemies_group.draw(screen)
    # Other drawing logic
