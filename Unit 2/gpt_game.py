import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
PLATFORM_WIDTH, PLATFORM_HEIGHT = 200, 10
FLOOR_HEIGHT = 10
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
FPS = 60
GRAVITY = 1

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer")

# Player setup
player = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)  # Slightly above the floor
player_speed = 5
player_y_velocity = 0
player_on_ground = False  # The player is initially not on the ground

# Custom platforms setup
custom_platforms = [
    pygame.Rect(150, 450, PLATFORM_WIDTH, PLATFORM_HEIGHT),
    pygame.Rect(400, 375, PLATFORM_WIDTH, PLATFORM_HEIGHT),
    pygame.Rect(650, 300, PLATFORM_WIDTH, PLATFORM_HEIGHT)
]

# Floor setup
floor = pygame.Rect(0, SCREEN_HEIGHT - FLOOR_HEIGHT, SCREEN_WIDTH, FLOOR_HEIGHT)

# Function to check collision with platforms and floor
def check_collision():
    global player_y_velocity, player_on_ground
    on_ground = False

    # Check collision with custom platforms
    for platform in custom_platforms:
        if player.colliderect(platform) and player.bottom >= platform.top and player_y_velocity >= 0:
            player.y = platform.top - player.height
            player_y_velocity = 0
            on_ground = True

    # Check collision with the floor
    if player.colliderect(floor) and player.bottom >= floor.top and player_y_velocity >= 0:
        player.y = floor.top - player.height
        player_y_velocity = 0
        on_ground = True

    player_on_ground = on_ground

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:  # A for left
        player.x -= player_speed
    if keys[pygame.K_d]:  # D for right
        player.x += player_speed
    if keys[pygame.K_w]:  # W for jump when on the ground
        player_y_velocity = -15  # Jump velocity

    # Apply gravity
    if not player_on_ground:
        player_y_velocity += GRAVITY

    # Keep player on screen horizontally
    if player.left <= 0:
        player.left = 0
    if player.right >= SCREEN_WIDTH:
        player.right = SCREEN_WIDTH

    # Check collision with custom platforms and the floor
    check_collision()

    # Game display
    screen.fill(WHITE)

    # Draw custom platforms
    for platform in custom_platforms:
        pygame.draw.rect(screen, GREEN, platform)

    # Draw floor
    pygame.draw.rect(screen, GREEN, floor)

    # Draw player
    pygame.draw.rect(screen, BLUE, player)

    # Update display
    pygame.display.flip()

    # Tick
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
