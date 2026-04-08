import pygame
import random


class Raindrop:
    __slots__ = ("x", "y", "radius")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 1

    def update(self):
        self.radius += 1

    def draw(self, window):
        pygame.draw.circle(window, (0, 0, 255), (self.x, self.y), self.radius)



class RaindropsManager:
    RAIN_RATE = 500      # milliseconds
    MAX_RADIUS = 40

    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Raindrops")

        self.clock = pygame.time.Clock()
        self.raindrops = []
        self.last_time = pygame.time.get_ticks()

    def run(self):
        running = True
        while running:

            # -------- Event Handling --------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # -------- Add Raindrops --------
            current_time = pygame.time.get_ticks()
            if current_time - self.last_time >= RaindropsManager.RAIN_RATE:
                x = random.randint(0, self.width)
                y = random.randint(0, self.height)
                self.raindrops.append(Raindrop(x, y))
                self.last_time = current_time

            # -------- Update Raindrops --------
            for drop in self.raindrops:
                drop.update()

            # -------- Remove Large Raindrops --------
            self.raindrops = [
                drop for drop in self.raindrops
                if drop.radius <= RaindropsManager.MAX_RADIUS
            ]

            # -------- Draw --------
            self.window.fill((0, 0, 0))
            for drop in self.raindrops:
                drop.draw(self.window)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


# -----------------------------
# Driver Code
# -----------------------------
manager = RaindropsManager()
manager.run()