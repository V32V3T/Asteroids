from circleshape import CircleShape
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
    
    def collides_with(self, other):
        distance = (self.position - other.position).length()
        return distance <= (self.radius + other.radius)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        x=random.uniform(20,50)
        new_velocity1 = self.velocity.copy().rotate(x)
        new_velocity2 = self.velocity.copy().rotate(-x)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroidn1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroidn1.velocity = new_velocity1*1.2
        asteroidn2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroidn2.velocity = new_velocity2*1.2
        
        
        