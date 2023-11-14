# Importing Pygame and Initialization

import pygame
import random
pygame.init()

def show_start_screen():
    
    # Create a start screen
    screen.fill((255, 255, 255))
    title_font = pygame.font.SysFont('Wingdings', 40)
    title_text = title_font.render('Flappy Bird', False, (0, 0, 0))
    screen.blit(title_text, (200, 250))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

def show_game_over_screen(score):
    screen.fill((255, 255, 255))
    game_over_font = pygame.font.SysFont('Comic Sans MS', 40)
    game_over_text = game_over_font.render(f'get rekd m8 Score: {score}', False, (0, 0, 0))
    screen.blit(game_over_text, (150, 250))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

# Creating a Game Window

window_size = (1000, 500)

screen = pygame.display.set_mode(window_size)

pipe_width = 50 # width of the pipe visually
pipe_gap = 200 # gap so Flappy Bird can always make it through
pipe_height = random.randint(100, window_size[1]-100) # randomize the pipe height
pipe_x = window_size[0]  # Starting x-coordinate is edge of the screen

# create and load an upper pipe image
upper_pipe_image = pygame.image.load('C:/Users/rynog/OneDrive/Desktop/CS 101/Unit 2/Flappy Bird Game Obstacles/pipe.png')  # Make sure to have an image named 'pipe.png' in the same folder
upper_pipe_image = pygame.transform.flip(upper_pipe_image, False, True) # flip the image so it faces the correct direction

# create and load a lower pipe image
lower_pipe_image = pygame.image.load('C:/Users/rynog/OneDrive/Desktop/CS 101/Unit 2/Flappy Bird Game Obstacles/pipe.png')


# Load background image

bg_image = pygame.image.load('C:/Users/rynog/OneDrive/Desktop/CS 101/Unit 2/Flappy Bird Basics/bg.png')

# scale the background image to fit the game window size

bg_image = pygame.transform.scale(bg_image, (window_size[0], window_size[1]))

# Initialize background positions

bg_x1 = 0

bg_x2 = bg_image.get_width() # Assume the background image is the same width as the screen

# Scroll speed

bg_scroll_speed = 2



# Set the title of the window

pygame.display.set_caption('Super Bird')



# Initialize the font

pygame.font.init()

myfont = pygame.font.SysFont('Arial', 30)

# Create a text surface

text_surface = myfont.render('Score: 0', False, (0, 0, 0))



# Load an image

bird_image = pygame.image.load('C:/Users/rynog/OneDrive/Desktop/CS 101/Unit 2/Flappy Bird Basics/bird1.png') # Make sure to have an image named 'bird1.png' in the same folder

# Scale the image

bird_image = pygame.transform.scale(bird_image, (65, 50))



# Tells us where the bird is gonna be

bird_x = 50

bird_y = 50



# Bird flapping

bird_velocity = 0

flap_power = -15 # This will determine how much the bird will move upwards

gravity = 1

bird_rect = pygame.Rect(bird_x, bird_y, 65, 50)  # Assuming the bird image is 100x50 pixels create a rectangle "hitbox" for Flappy Bird

score = 0
# A Simple Game Loop

running = True

show_start_screen()

# Main game loop (keeps the window up and the game alive)

while running:

 

    # Event handler (what do we do with user input)

    for event in pygame.event.get():
    # quit  pressed
        if event.type == pygame.QUIT:
            running = False
        # space key pressed
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                bird_velocity = flap_power

    pipe_x -= 20 # move the pipe closer to the left of the screen
    if pipe_x < -pipe_width:
        # when the pipe reaches the edge of the screen we reset it with random parameters
        score += 1
        pipe_x = window_size[0]
        pipe_height = random.randint(100, window_size[1]-100)
        print(score)

    upper_pipe_rect = pygame.Rect(pipe_x, 0, pipe_width, pipe_height) # create the upper pipe
    lower_pipe_rect = pygame.Rect(pipe_x, pipe_height + pipe_gap, pipe_width, window_size[0]) # create the lower pipe

    if bird_rect.colliderect(upper_pipe_rect) or bird_rect.colliderect(lower_pipe_rect): # check for a collision
        show_game_over_screen(score)  # print game over if there is a collision
        bird_y = 250
        bird_velocity = 0
        score = 0
        pipe_x = window_size[0]
        pipe_height = random.randint(100, window_size[1]-100)

    # update bird velocity

    bird_velocity += gravity

    bird_y += bird_velocity

 

    if bird_y >= window_size[1]: # if Flappy Bird's position is greater than or equal to the height of the screen (hits the floor)
        
        show_game_over_screen(score)  # print game over if there is a collision
        bird_y = 250
        bird_velocity = 0
        score = 0
        pipe_x = window_size[0]
        pipe_height = random.randint(100, window_size[1]-100)
        # we will reset its position and velocity

        bird_y = 50

        bird_velocity = 0

    if bird_y <= 0: # if Flappy Bird hits the ceiling (y position is 0)

        # we lock his position at the top of the screen

        bird_y = 0

        bird_velocity = 0

    bird_rect.topleft = (bird_x, bird_y) # this will be Flappy Bird's hitbox and must be placed before the blit, notice how it matches the x,y


    # ** Game State Update **

    screen.fill((185, 217, 235)) # Fill the screen with white color

    

    # *** NEW CODE ***

    bg_x1 -= bg_scroll_speed # update background position

    bg_x2 -= bg_scroll_speed

    # *** NEW CODE ***

    if bg_x1 <= -bg_image.get_width(): # reset background position when it's fully off the screen

        bg_x1 = bg_image.get_width()

    if bg_x2 <= -bg_image.get_width():

        bg_x2 = bg_image.get_width()

    # *** NEW CODE ***

    screen.blit(bg_image, (bg_x1, 0)) # paints the background images
    screen.blit(bg_image, (bg_x2, 0))




    screen.blit(bird_image, (bird_x, bird_y))

    text_surface = myfont.render(f'Score: {score} ', False, (0, 0, 0))
    screen.blit(text_surface, (10, 10))

    # scale the upper/lower pipe images so they fit the hitboxes
    upper_pipe_image = pygame.transform.scale(upper_pipe_image, (pipe_width, pipe_height))
    lower_pipe_image = pygame.transform.scale(lower_pipe_image, (pipe_width, pipe_gap + pipe_height))
    
    # paint the upper/lower pipe images over the rectangle hit boxes
    screen.blit(upper_pipe_image, upper_pipe_rect.topleft)
    screen.blit(lower_pipe_image, lower_pipe_rect.topleft)

    # ** End Game State Update **
    pygame.display.flip() # Update the display

    # frame rate control
    pygame.time.delay(60)



pygame.quit()