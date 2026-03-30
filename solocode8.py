import pygame
import random

class Raindrop:
    __slots__ = ("x", "y", "radius")
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self.radius = 1 
    
    def draw(self, window): 
        pygame.draw.circle(window, (0, 0, 255), (self.x, self.y), self.radius, 1)
    
    def update(self):
        self.radius