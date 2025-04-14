import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self,surface, color, position, radius, width = 2):
        self.surface = surface
        self.position = position
        self.radius = radius
        self.width = width
        self.color = "white"
        pygame.draw.circle(self.surface, 
                           self.color, 
                           self.position, 
                           self.radius, 
                           self.width
                           )
