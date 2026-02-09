import pygame
import random
import sys

# --------------------
# Helper function (from assignment)
# --------------------
def draw_text(surface, text, x, y, color, font_size=24):
    text_font = pygame.font.SysFont(None, font_size)
    text_surface = text_font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

# --------------------
# Initialize pygame
# --------------------
pygame.init()
pygame.mixer.init()

# --------------------
# Window setup
# --------------------
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Click the Bouncing Ball!")

clock = pygame.time.Clock()

# --------------------
# Colors
# --------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# --------------------
# Load sound (choose any sound you like)
# --------------------
success_sound = pygame.mixer.Sound("boing.wav")

# --------------------
# Ball setup
# --------------------
BALL_RADIUS = 25
ball_x = random.randint(BALL_RADIUS, WINDOW_WIDTH - BALL_RADIUS)
ball_y = random.randint(BALL_RADIUS, WINDOW_HEIGHT - BALL_RADIUS)

xSpeed = random.choice([-3, 3])
ySpeed = random.choice([-3, 3])

ball_rect = pygame.Rect(
    ball_x - BALL_RADIUS,
    ball_y - BALL_RADIUS,
    BALL_RADIUS * 2,
    BALL_RADIUS * 2
)

# --------------------
# Game variables
# --------------------
score = 0
game_over = False

start_time = pygame.time.get_ticks()  # record game start time
end_time = 0

# --------------------
# Main game loop
# --------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_pos = event.pos
            if ball_rect.collidepoint(mouse_pos):
                # Successful click
                score += 1
                success_sound.play()

                # Reset ball position
                ball_x = random.randint(BALL_RADIUS, WINDOW_WIDTH - BALL_RADIUS)
                ball_y = random.randint(BALL_RADIUS, WINDOW_HEIGHT - BALL_RADIUS)

                # Increase speed randomly between 1 and 5
                xSpeed += random.randint(1, 5) * (1 if xSpeed > 0 else -1)
                ySpeed += random.randint(1, 5) * (1 if ySpeed > 0 else -1)

                # Check for game over
                if score >= 5:
                    game_over = True
                    end_time = pygame.time.get_ticks()

    # --------------------
    # Update ball movement
    # --------------------
    if not game_over:
        ball_x += xSpeed
        ball_y += ySpeed

        # Bounce off walls
        if ball_x <= BALL_RADIUS or ball_x >= WINDOW_WIDTH - BALL_RADIUS:
            xSpeed = -xSpeed
        if ball_y <= BALL_RADIUS or ball_y >= WINDOW_HEIGHT - BALL_RADIUS:
            ySpeed = -ySpeed

        ball_rect.center = (ball_x, ball_y)

    # --------------------
    # Drawing
    # --------------------
    window.fill(WHITE)

    # Draw score
    draw_text(window, f"Score: {score}", 10, 10, BLACK)

    if not game_over:
        pygame.draw.circle(window, RED, (ball_x, ball_y), BALL_RADIUS)
    else:
        elapsed_time = (end_time - start_time) / 1000
        draw_text(
            window,
            f"You won! Time: {elapsed_time:.2f} seconds",
            WINDOW_WIDTH // 2 - 170,
            WINDOW_HEIGHT // 2,
            BLACK,
            font_size=36
        )

    pygame.display.update()
    clock.tick(60)