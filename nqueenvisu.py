import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set up display variables
board_size = 6
square_size = 60
width, height = board_size * square_size, board_size * square_size
black, white = (0, 0, 0), (255, 255, 255)
red, blue = (255, 0, 0), (0, 0, 255)

# Create the screen object
screen = pygame.display.set_mode((width, height))

# Load Queen Image
queen_img = pygame.image.load('queen.png')
queen_img = pygame.transform.scale(queen_img, (square_size, square_size))

# Draw the chessboard
def draw_board(board):
    for row in range(board_size):
        for col in range(board_size):
            color = white if (row + col) % 2 == 0 else black
            pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))
            if board[row][col] == 1:
                screen.blit(queen_img, (col * square_size, row * square_size))

    pygame.display.update()
    time.sleep(0.5)  # Delay for visualization

# Check if a position is safe for the queen
def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, board_size, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# Solve the N-Queens problem
def solve_nqueens(board, col):
    if col >= board_size:
        return True

    for i in range(board_size):
        if is_safe(board, i, col):
            board[i][col] = 1
            draw_board(board)

            if solve_nqueens(board, col + 1):
                return True

            board[i][col] = 0
            draw_board(board)

    return False

def main():
    board = [[0 for _ in range(board_size)] for _ in range(board_size)]
    solve_nqueens(board, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
