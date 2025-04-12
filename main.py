# this allows us to use code from
# the open-source pygame library
# throughout this file
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS 

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # infinite loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
