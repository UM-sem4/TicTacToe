import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions and title
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic-Tac-Toe")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
grey = (200, 200, 200)

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 34)

# Game variables
player = 'X'
board = [['' for _ in range(3)] for _ in range(3)]
game_over = False
winner = None
x_wins = 0
o_wins = 0


def draw_board():
    screen.fill(white)
    # Draw grid lines
    pygame.draw.line(screen, black, (200, 0), (200, 600), 5)
    pygame.draw.line(screen, black, (400, 0), (400, 600), 5)
    pygame.draw.line(screen, black, (0, 200), (600, 200), 5)
    pygame.draw.line(screen, black, (0, 400), (600, 400), 5)

    # Draw symbols
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                color = blue
            elif board[row][col] == 'O':
                color = red
            else:
                continue
            text = font.render(board[row][col], True, color)
            screen.blit(text, (col * 200 + 55, row * 200 + 55))

    # Display status messages
    if game_over:
        popup_message()
    else:
        status_text = f"Player {player}'s turn"
        status_message = small_font.render(status_text, True, black)
        screen.blit(status_message, (20, 560))

    # Display win counters
    x_win_counter_text = f"X Wins: {x_wins}"
    o_win_counter_text = f"O Wins: {o_wins}"
    x_win_counter_message = small_font.render(x_win_counter_text, True, black)
    o_win_counter_message = small_font.render(o_win_counter_text, True, black)
    screen.blit(x_win_counter_message, (20, 20))
    screen.blit(o_win_counter_message, (400, 20))


def popup_message():
    pygame.draw.rect(screen, grey, (100, 200, 400, 200))
    message = f"{winner} wins!" if winner else "It's a draw!"
    text = small_font.render(message, True, black)
    screen.blit(text, (220, 250))
    restart_text = small_font.render("Press 'R' to restart", True, black)
    screen.blit(restart_text, (180, 300))


def check_winner():
    global winner, game_over, x_wins, o_wins
    # Check rows, columns and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            winner = board[i][0]
            game_over = True
            return
        if board[0][i] == board[1][i] == board[2][i] != '':
            winner = board[0][i]
            game_over = True
            return
    if board[0][0] == board[1][1] == board[2][2] != '':
        winner = board[0][0]
        game_over = True
        return
    if board[0][2] == board[1][1] == board[2][0] != '':
        winner = board[0][2]
        game_over = True
        return
    # Check for draw
    if all(board[row][col] != '' for row in range(3) for col in range(3)):
        game_over = True


def reset_game():
    global board, player, game_over, winner
    board = [['' for _ in range(3)] for _ in range(3)]
    player = 'X'
    game_over = False
    winner = None


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            row, col = y // 200, x // 200
            if board[row][col] == '':
                board[row][col] = player
                check_winner()
                if game_over:
                    if winner == 'X':
                        x_wins += 1
                    elif winner == 'O':
                        o_wins += 1
                else:
                    player = 'O' if player == 'X' else 'X'
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()

    draw_board()
    pygame.display.flip()
