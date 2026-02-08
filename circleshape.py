import pygame
from player import *
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):

        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius


    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
       # must override
        pass

    def collides_with(self, other):
        # distance_to_other = pygame.Vector2.distance_to(self.position, other.position)
        distance_to_other = self.position.distance_to(other.position)
        combined_radius = self.radius + other.radius
        return distance_to_other <= combined_radius

    def out_of_bonds(self):
        return (self.position.x < -self.radius or 
        self.position.x > SCREEN_WIDTH + self.radius or
        self.position.y < -self.radius or 
        self.position.y > SCREEN_HEIGHT + self.radius)