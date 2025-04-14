import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        super().__init__(self.x,self.y,PLAYER_RADIUS)
        self.rotation = 0

 # draw function
    def draw(self, screen):
        pygame.draw.polygon(self.screen,"white", self.triangle(), width = 2)

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]    
    
    # rotate
    def rotate(self, dt):
        self.dt = dt
        self.rotation + PLAYER_TURN_SPEED * self.dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            # rotate right
            self.rotate(dt)
    
        if keys[pygame.K_d]:
            # ?
            self.rotate((-1)*dt)