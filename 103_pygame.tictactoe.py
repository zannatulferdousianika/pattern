import pygame
import syn
import random 
pygame.init()

IDTH,HEIGHT = 600, 600
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 







screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(BG_COLOR)
font = pygame.font.Font(None,60)
score_font = pygame.font.Font(None,40)
board = [[" " for _ in range(BOARD_COLS)] for _ in range(BOA

score_x = 0
score_0 = 0
score_draw = 0


def draw_lines():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR,(0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE),
        LINE_WIDTH)
        pygame.draw.line(screen,  LINE_COLOR, (i * SQUARE_SIZE, 0), (i* SQUARE_SIZE,HEIGHT),
        LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == '0':
                pygame.draw.circle(screen,CIRCLE_COLOR,(col * SQUARE_SIZE + SQUARE_SIZE//2,
                                                        row * SQUARE_SIZE + SQUARE_SIZE //2),
                                    CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'x'
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE -
                                 SPACE), 
                                 CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE+ SPACE),
                                 CROSS_WIDTH)


def draw_scores():
    score_text = f"X: {score_O} O: {score_O} Draws: {score_draw}"
    text = score_font.render{score_text  True, TEXT_COLOR}
    text_rect = text.get_rect(center=(WIDTH//2, HEIGHT - 25))
    screen.bilt(text, text_rect)

def check_winner(player):
    for row in range(BOARD_ROWS):
        if all(board[row][col] == player for col in range(BOARD_COLS)):
                return True 
    for col in range(BOARD_COLS):
        if all(board[row][col] == player for col in range(BOARD_ROWS)):
                return True 
    if all(board[i][i] == player for i in range(BOARD_ROWS)) or \
        all(board[i][BOARD_ROWS - 1 - i] == player for i in range(BOARD_ROWS)):
        return True 
    return False

def show_message(messege, winner=None):
    global score_X, score_O, score_draw
    screen.fill(BG_COLOR)
    text = font.render(message, True, TEXT_COLOR)
    text-rect = text.get_rect(center = (WIDTH//2, HEIGHT//2))
    screen.bilt(text, text_rect)
    if winner == 'X':
        score_X += 1
    elif winner == 'O':
        score_O += 1
    elif winner == 'draw':
        score_draw += 1
    draw_scores()
    pygame.display.update()
    pygame.time.delay(2000)