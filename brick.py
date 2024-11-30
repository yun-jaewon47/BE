import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Game")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# 공 속성
ball_radius = 10
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x, ball_speed_y = 4, 4

# 패들 속성
paddle_width, paddle_height = 100, 10
paddle_x = WIDTH // 2 - paddle_width // 2
paddle_y = HEIGHT - 30
paddle_speed = 6

# 벽돌 속성
brick_rows, brick_cols = 5, 10
brick_width = WIDTH // brick_cols
brick_height = 20
bricks = [[1 for _ in range(brick_cols)] for _ in range(brick_rows)]

# 폰트 설정
font = pygame.font.Font(None, 36)

# 게임 루프
clock = pygame.time.Clock()
running = True
score = 0

while running:
    screen.fill(BLACK)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    # 공 이동
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 벽 충돌
    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
        ball_speed_x = -ball_speed_x
    if ball_y - ball_radius < 0:
        ball_speed_y = -ball_speed_y

    # 패들 충돌
    if paddle_y < ball_y + ball_radius < paddle_y + paddle_height and \
       paddle_x < ball_x < paddle_x + paddle_width:
        ball_speed_y = -ball_speed_y

    # 벽돌 충돌
    for row in range(brick_rows):
        for col in range(brick_cols):
            if bricks[row][col]:
                brick_x = col * brick_width
                brick_y = row * brick_height
                if brick_x < ball_x < brick_x + brick_width and \
                   brick_y < ball_y < brick_y + brick_height:
                    ball_speed_y = -ball_speed_y
                    bricks[row][col] = 0
                    score += 1

    # 공이 화면 아래로 떨어짐
    if ball_y > HEIGHT:
        running = False

    # 벽돌 그리기
    for row in range(brick_rows):
        for col in range(brick_cols):
            if bricks[row][col]:
                brick_x = col * brick_width
                brick_y = row * brick_height
                pygame.draw.rect(screen, RED, (brick_x, brick_y, brick_width, brick_height))

    # 패들 그리기
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))

    # 공 그리기
    pygame.draw.circle(screen, GREEN, (ball_x, ball_y), ball_radius)

    # 점수 표시
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
