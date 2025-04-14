import sys
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ceas = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    # game's groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    
    Asteroid.containers = (asteroids, updatable,drawable)
    AsteroidField.containers = updatable
    
    Player.containers = (updatable, drawable)
    
    pl = Player(x,y)
    astfld = AsteroidField()

    # infinite loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #pl.update(dt)
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(pl):
                print("Game over!")
                sys.exit()

        for shot in shots:
            if asteroid.collides_with(shot):
                shot.kill()
                asteroid.kill()

        screen.fill("black")

        #pl.draw(screen)
        for obj in drawable:
            obj.draw(screen)


        pygame.display.flip()

        dt = ceas.tick(60)/1000

if __name__ == "__main__":
    main()
