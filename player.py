import pygame
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        super().__init__(self.x,self.y, PLAYER_RADIUS)
        self.rotation = 0

 # draw function
    def draw(self, screen):
        self.screen = screen
        pygame.draw.polygon(self.screen,"white", self.triangle(), width = 2)

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]    

    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            # rotate right
            self.rotate(-dt)
    
        if keys[pygame.K_d]:
            # rotate left
            self.rotate(dt)

        if keys[pygame.K_w]:
            # move up
            self.move(dt)
    
        if keys[pygame.K_s]:
            #  move down
            self.move(-dt)    
        
        if keys[pygame.K_SPACE]:
            # shooooot
            self.shoot()

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED        

    # rotate
    def rotate(self, dt):
        self.dt = dt
        self.rotation += PLAYER_TURN_SPEED * self.dt

    # move
    def move(self, dt):
        self.dt = dt
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * self.dt