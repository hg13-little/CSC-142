import pygame
import random
from Ball import Ball

pygame.init()

# Window setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click the Balls Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

# Game variables
ballList = []
score = 0

startTicks = pygame.time.get_ticks()
lastSeconds = 0

running = True
while running:
    screen.fill((200, 200, 255))

    elapsedSeconds = (pygame.time.get_ticks() - startTicks) // 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            for ball in ballList[:]:
                if ball.rect.collidepoint(mousePos):
                    ballList.remove(ball)
                    score += 1

    # Add a new ball every second
    if elapsedSeconds > lastSeconds:
        lastSeconds = elapsedSeconds
        ballList.append(Ball(screen, WIDTH, HEIGHT))

    # Move and draw balls
    for ball in ballList:
        ball.update()
        ball.draw()

    # Draw score and time
    scoreText = font.render(f"Score: {score}", True, (0, 0, 0))
    timeText = font.render(f"Time: {elapsedSeconds}", True, (0, 0, 0))
    screen.blit(scoreText, (10, 10))
    screen.blit(timeText, (10, 40))

    # End game after 15 seconds
    if elapsedSeconds >= 15:
        ballList.clear()
        gameOverText = font.render(
            f"Game Over! Final Score: {score}", True, (255, 0, 0)
        )
        screen.blit(gameOverText, (200, 300))
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()