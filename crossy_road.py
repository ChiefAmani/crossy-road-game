import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Crossy Road")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Player properties
PLAYER_SIZE = 30
player_x = SCREEN_WIDTH // 2 - PLAYER_SIZE // 2
player_y = SCREEN_HEIGHT - PLAYER_SIZE - 10
player_speed = 5

# Obstacle properties
OBSTACLE_WIDTH = 100
OBSTACLE_HEIGHT = 40
obstacle_speed = 3
obstacles = []

# Game variables
score = 0
font = pygame.font.Font(None, 36)

def draw_player(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, PLAYER_SIZE, PLAYER_SIZE))

def draw_obstacle(x, y):
    pygame.draw.rect(screen, RED, (x, y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

def create_obstacle():
    x = random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH)
    y = random.random() * -SCREEN_HEIGHT - OBSTACLE_HEIGHT # Start off-screen
    speed = random.randint(2, 5)
    obstacles.append({"rect": pygame.Rect(x, y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT), "speed": speed})

# Initial obstacles
for _ in range(5):
    create_obstacle()

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= player_speed * 10
            if event.key == pygame.K_RIGHT:
                player_x += player_speed * 10
            if event.key == pygame.K_UP:
                player_y -= player_speed * 10
            if event.key == pygame.K_DOWN:
                player_y += player_speed * 10

    # Player boundaries
    if player_x < 0:
        player_x = 0
    if player_x > SCREEN_WIDTH - PLAYER_SIZE:
        player_x = SCREEN_WIDTH - PLAYER_SIZE
    if player_y < 0:
        player_y = 0
    if player_y > SCREEN_HEIGHT - PLAYER_SIZE:
        player_y = SCREEN_HEIGHT - PLAYER_SIZE

    # Move obstacles
    for obstacle in obstacles:
        obstacle["rect"].y += obstacle["speed"]
        if obstacle["rect"].y > SCREEN_HEIGHT:
            obstacles.remove(obstacle)
            create_obstacle()
            score += 1

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle["rect"]):
            print("Game Over! Score:", score)
            running = False

    # Drawing
    screen.fill(BLACK)
    draw_player(player_x, player_y)
    for obstacle in obstacles:
        draw_obstacle(obstacle["rect"].x, obstacle["rect"].y)

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()