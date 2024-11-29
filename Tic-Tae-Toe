import pygame
import sys

# 초기 설정
pygame.init()
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 게임 변수
CELL_SIZE = WIDTH // 3
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"
winner = None
game_over = False

# 폰트 설정
FONT = pygame.font.Font(None, 80)
SMALL_FONT = pygame.font.Font(None, 40)

def draw_board():
    SCREEN.fill(WHITE)
    # 세로선
    pygame.draw.line(SCREEN, BLACK, (CELL_SIZE, 0), (CELL_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(SCREEN, BLACK, (2 * CELL_SIZE, 0), (2 * CELL_SIZE, HEIGHT), LINE_WIDTH)
    # 가로선
    pygame.draw.line(SCREEN, BLACK, (0, CELL_SIZE), (WIDTH, CELL_SIZE), LINE_WIDTH)
    pygame.draw.line(SCREEN, BLACK, (0, 2 * CELL_SIZE), (WIDTH, 2 * CELL_SIZE), LINE_WIDTH)

def draw_marks():
    for row in range(3):
        for col in range(3):
            mark = board[row][col]
            if mark == "X":
                color = RED
            elif mark == "O":
                color = BLUE
            else:
                continue
            text = FONT.render(mark, True, color)
            SCREEN.blit(text, (col * CELL_SIZE + CELL_SIZE // 3, row * CELL_SIZE + CELL_SIZE // 4))

def check_winner():
    global winner, game_over
    # 행, 열 확인
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            winner = board[i][0]
            pygame.draw.line(SCREEN, BLACK, (0, i * CELL_SIZE + CELL_SIZE // 2), (WIDTH, i * CELL_SIZE + CELL_SIZE // 2), LINE_WIDTH)
            game_over = True
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            winner = board[0][i]
            pygame.draw.line(SCREEN, BLACK, (i * CELL_SIZE + CELL_SIZE // 2, 0), (i * CELL_SIZE + CELL_SIZE // 2, HEIGHT), LINE_WIDTH)
            game_over = True
    # 대각선 확인
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        winner = board[0][0]
        pygame.draw.line(SCREEN, BLACK, (0, 0), (WIDTH, HEIGHT), LINE_WIDTH)
        game_over = True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        winner = board[0][2]
        pygame.draw.line(SCREEN, BLACK, (WIDTH, 0), (0, HEIGHT), LINE_WIDTH)
        game_over = True
    # 무승부 확인
    if not any(" " in row for row in board) and not winner:
        game_over = True

def display_winner():
    if winner:
        text = SMALL_FONT.render(f"{winner} wins!", True, BLACK)
    else:
        text = SMALL_FONT.render("It's a draw!", True, BLACK)
    SCREEN.blit(text, (WIDTH // 4, HEIGHT // 2))

# 게임 루프
def game_loop():
    global current_player
    running = True
    while running:
        draw_board()
        draw_marks()
        if game_over:
            display_winner()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                row, col = y // CELL_SIZE, x // CELL_SIZE
                if board[row][col] == " ":
                    board[row][col] = current_player
                    check_winner()
                    current_player = "O" if current_player == "X" else "X"

game_loop()
