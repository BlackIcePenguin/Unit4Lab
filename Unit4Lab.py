import pygame
import math
import random

# Color Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
COLORS = [RED, GREEN, BLUE, WHITE]

# Create Math Constant
PI = math.pi

# To convert from Degrees to Radians -> angle * (pi / 180)

# Game Constants
SIZE = (700, 500)
FPS = 60


# --------------------------------------------------------------------------- #
pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Pygame Lab')

clock = pygame.time.Clock()
day_night = 0
am = True


def sky_color(time):
    sky_color = (0, 190 * time / 3600, 255 * time / 3600)
    return sky_color


running = True

while running:
    # Get all input events (Keyboard, Mouse, Joystick, etc
    for event in pygame.event.get():

        # Look for specific event
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print('You Pressed a key')
        elif event.type == pygame.KEYUP:
            print('You Released a key')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('You Clicked the mouse')

    # Game logic (Objects fired, object movement) goes here

    screen.fill(sky_color(day_night))
    if day_night < 3600 and am is True:
        day_night += 1
    elif day_night < 3600 and am is False:
        day_night -= 1
    elif day_night == 3600:
        day_night -= 1
        am = False
    elif day_night == 0 and am is False:
        am = True
        day_night += 1

    # Add drawings here

    pygame.display.flip()

    clock.tick(FPS)


# Runs when main game loop ends
pygame.quit()