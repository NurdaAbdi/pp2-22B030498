import pygame

pygame.init()
BALL_SIZE = 50
BALL_RADIUS = 25
ball_x = 800 // 2
ball_y = 600 // 2
MOVEMENT_SPEED = 20
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("TASK 3")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y = max(ball_y - MOVEMENT_SPEED, BALL_RADIUS)
            elif event.key == pygame.K_DOWN:
                ball_y = min(ball_y + MOVEMENT_SPEED, 600 - BALL_RADIUS)
            elif event.key == pygame.K_LEFT:
                ball_x = max(ball_x - MOVEMENT_SPEED, BALL_RADIUS)
            elif event.key == pygame.K_RIGHT:
                ball_x = min(ball_x + MOVEMENT_SPEED, 800 - BALL_RADIUS)
    screen.fill('white')
    pygame.draw.circle(screen, 'red', (ball_x, ball_y), BALL_RADIUS)
    pygame.display.flip()
pygame.quit()
