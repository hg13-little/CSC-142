# Originally by Irv Kalb from Chapter 6 of Object-Oriented Python
# Modified by David Kopec to move in an arc

import pygame
from pygame.locals import *
import random
from math import sin

# Ball class 
class Ball():

    def __init__(self, window, windowWidth, windowHeight):
        self.window = window  # remember the window, so we can draw later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.image = pygame.image.load('ball.png')
        # A rect is made up of [x, y, width, height]
        self.ballRect = self.image.get_rect()
        self.ballRect = self.rect 
        self.width = self.ballRect.width
        self.height = self.ballRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height
        
        # Pick a random starting position 
        self.x = random.randrange(0, self.maxWidth)
        self.y = self.height

        # Choose a random speed between -4 and 4, but not zero
        # in both the x and y directions
        speedsList = [-7, -6, -5, -4, -3, 3, 4, 5, 6, 7] 
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.randrange(self.maxHeight, self.windowHeight * 2)

    def update(self):
        # Check for hitting a wall.  If so, change that direction.
        if (self.x < -self.width) or (self.x >= self.windowWidth):
            self.xSpeed = -self.xSpeed


        # Update the Ball's x and y, using the speed in two directions
        self.x = self.x + self.xSpeed
import pygame
import random
from math import sin

class Ball:

    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.image = pygame.image.load('ball.png')

        # CREATE RECT (this fixes your error)
        self.rect = self.image.get_rect()
        self.ballRect = self.rect  # alias for older code

        self.width = self.rect.width
        self.height = self.rect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height

        # Random start
        self.x = random.randrange(0, self.maxWidth)
        self.y = self.height

        speedsList = [-7, -6, -5, -4, -3, 3, 4, 5, 6, 7]
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.randrange(self.maxHeight, self.windowHeight * 2)

        # Sync rect position
        self.rect.topleft = (self.x, self.y)

    def update(self):
        # Bounce off side walls
        if self.x < -self.width or self.x >= self.windowWidth:
            self.xSpeed *= -1

        # Move in arc
        self.x += self.xSpeed
        self.y = self.windowWidth - self.ySpeed * sin(3.14 * self.x / self.maxWidth)

        # ALWAYS sync rect
        self.rect.topleft = (self.x, self.y)

    def draw(self):
        self.window.blit(self.image, self.rect)
        self.ballRect.y = self.y

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))
