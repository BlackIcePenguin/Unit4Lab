import pygame
import math
import random

# Color Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_GREEN = (11, 46, 2)
BROWN = (41, 21, 2)
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


# Setting the sky loop color
def sky_color(time):
    sky_color = (0, 190 * time / 1800, 255 * time / 1800)
    return sky_color
# Tree, based on bottom right point on tree for x


def tree_builder(x, y):
    pygame.draw.rect(screen, BROWN, [x-20, y-80, 20, 80], width=0)
    for number in range(0, 2):
        pygame.draw.polygon(screen, DARK_GREEN, [(x-60, y-60-60*number), (x+40, y-60-60*number),
                                                 (x-10, y-180-(60*number))], width=0)


running = True

while running:
    # Get all input events (Keyboard, Mouse, Joystick, etc
    for event in pygame.event.get():

        # Look for specific event
        if event.type == pygame.QUIT:
            running = False

    # Game logic (Objects fired, object movement) goes here

    # Setting the sky and its change, full loop every minute
    screen.fill(sky_color(day_night))
    if day_night < 1800 and am is True:
        day_night += 1
    elif day_night < 1800 and am is False:
        day_night -= 1
    elif day_night == 1800:
        day_night -= 1
        am = False
    elif day_night == 0 and am is False:
        am = True
        day_night += 1

    # Add drawings here
    pygame.draw.rect(screen, GREEN, [0, 400, 700, 500], width=0)
    for num in range(0, 4):
        pygame.draw.ellipse(screen, WHITE, [80 + 180*num, 100 - 10*num, 120, 60], width=0)
    for val in range(0, 6):
        tree_builder(70 + 115*val, 400)

    pygame.display.flip()

    clock.tick(FPS)


# Runs when main game loop ends
pygame.quit()
