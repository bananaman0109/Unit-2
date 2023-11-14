import pygame 
import random # Initialize Pygame 
pygame.init() # Constants 
WIDTH, HEIGHT = 800, 600 
BIRD_WIDTH, BIRD_HEIGHT = 50, 50 
PIPE_WIDTH, PIPE_HEIGHT = 100, 400 PIPE_GAP = 200 
GRAVITY = 0.5 
BIRD_JUMP = 10 # Colors 
WHITE = (255, 255, 255) # Create the screen 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Flappy Bird") # Load bird image bird_img = pygame.image.load("bird.png") bird_img = pygame.transform.scale(bird_img, (BIRD_WIDTH, BIRD_HEIGHT)) # Create bird bird_x = 100 bird_y = HEIGHT // 2 bird_velocity = 0 # Create pipes pipes = [] pipe_x = WIDTH pipe_speed = 5 # Game loop running = True while running: for event in pygame.event.get(): if event.type == pygame.QUIT: running = False if event.type == pygame.KEYDOWN: if event.key == pygame.K_SPACE: bird_velocity = -BIRD_JUMP bird_y += bird_velocity bird_velocity += GRAVITY # Create new pipes if pipe_x <= WIDTH - PIPE_WIDTH: pipe_height = random.randint(100, HEIGHT - PIPE_GAP - 100) pipes.append((pipe_x, pipe_height)) pipe_x += 300 # Move and remove pipes for i in range(len(pipes)): pipes[i] = (pipes[i][0] - pipe_speed, pipes[i][1]) if pipes[i][0] < -PIPE_WIDTH: pipes.pop(i) # Draw the background screen.fill(WHITE) # Draw bird screen.blit(bird_img, (bird_x, bird_y)) # Draw pipes for pipe in pipes: pygame.draw.rect(screen, (0, 128, 0), (pipe[0], 0, PIPE_WIDTH, pipe[1])) pygame.draw.rect(screen, (0, 128, 0), (pipe[0], pipe[1] + PIPE_GAP, PIPE_WIDTH, HEIGHT - pipe[1] - PIPE_GAP)) pygame.display.update() # Quit Pygame pygame.quit()
