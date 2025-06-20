from circleshape import *
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
       super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    

    def update(self, dt):
        self.position += self.velocity * dt
    

    def split(self, dt):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)

        first_vector = self.velocity.rotate(angle)
        second_vector = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        ast_one = Asteroid(self.position.x, self.position.y, new_radius) 
        ast_two = Asteroid(self.position.x, self.position.y, new_radius)

        ast_one.velocity = first_vector * 1.2 
        ast_two.velocity = second_vector 
