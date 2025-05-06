
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Initialize the game board
board = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Function to draw the grid lines
def draw_grid():
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 2)
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 2)

# Function to draw X or O in a cell
def draw_symbol(row, col, symbol):
    font = pygame.font.Font(None, 100)
    text = font.render(symbol, True, BLACK)
    text_rect = text.get_rect(center=((col * CELL_SIZE) + CELL_SIZE // 2, (row * CELL_SIZE) + CELL_SIZE // 2))
    screen.blit(text, text_rect)

# Function to check for a win
def check_winner(symbol):
    for i in range(GRID_SIZE):
        if all(board[i][j] == symbol for j in range(GRID_SIZE)) or all(board[j][i] == symbol for j in range(GRID_SIZE)):
            return True
    if all(board[i][i] == symbol for i in range(GRID_SIZE)) or all(board[i][GRID_SIZE - i - 1] == symbol for i in range(GRID_SIZE)):
        return True
    return False

# Function to check for draw
def check_draw():
    return all(all(cell != '' for cell in row) for row in board)

# Game loop
running = True
current_player = 'X'
game_over = False

while running:
    screen.fill(WHITE)
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = y // CELL_SIZE
            col = x // CELL_SIZE

            if board[row][col] == '':
                board[row][col] = current_player
                if check_winner(current_player):
                    print(f"Player {current_player} wins!")
                    game_over = True
                elif check_draw():
                    print("It's a draw!")
                    game_over = True
                else:
                    current_player = 'O' if current_player == 'X' else 'X'

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] != '':
                draw_symbol(i, j, board[i][j])

    pygame.display.flip()

pygame.quit()
sys.exit()
