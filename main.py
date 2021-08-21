import numpy as np
import random
import pygame
import pygame_menu
import sys
import math
import button

# Symbolic constants
BOARD_HEIGHT = 14
BOARD_WIDTH = 14
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
START_HEIGHT = 60
START_WIDTH = 145
BLOCK_SIZE = 25
WHITE = (255, 255, 255)
RED = (255, 0, 0)
MAROON = (168,140,148)
# FONT = pygame.font.SysFont('Corbel',35)


# initializing the window
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
window = pygame.display.set_mode(size)


# function to determine if a piece had won
def isWin(array, piece):
    for row in range(15):
        for col in range(15):
            # check horizontal 5 in a row
            if col < 11 and array[row][col] == piece and array[row][col + 1] == piece and array[row][
                col + 2] == piece and array[row][
                col + 3] == piece and array[row][col + 4] == piece:
                return True
            # check vertical 5 in a row
            if row < 11 and array[row][col] == piece and array[row + 1][col] == piece and array[row + 2][
                col] == piece and array[row + 3][
                col] == piece and array[row + 4][col] == piece:
                return True
            # check diagonal pos slope 5 in a row
            if (row > 3 and col < 11) and array[row][col] == piece and array[row - 1][col + 1] == piece and \
                    array[row - 2][col + 2] == piece and array[row - 3][
                col + 3] == piece and array[row - 4][col + 4] == piece:
                return True
            # check diagonal neg slope 5 in a row
            if (row < 11 and col < 11) and array[row][col] == piece and array[row + 1][col + 1] == piece and \
                    array[row + 2][col + 2] == piece and array[row + 3][
                col + 3] == piece and array[row + 4][col + 4] == piece:
                return True


def button(screen, position, text):
    font = pygame.font.SysFont("Corbel", 20)
    text_render = font.render(text, 0, (0, 0, 0))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (255, 255, 255), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (255, 255, 255), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (255, 255, 255), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (255, 255, 255), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, (255, 255, 255, 0.8), (x, y, w, h))
    return screen.blit(text_render, (x, y))


# Human vs. human implementation
def humanVsHuman():
    # set screen
    black = (0, 0, 0)
    window.fill(black)

    # Game variables
    game_over = False
    turn = 0
    is_winner = 0

    # Create grids (Array and GUI)
    gridArr = np.zeros((15, 15))
    print(gridArr)
    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            pygame.draw.rect(window, WHITE,
                             (i * BLOCK_SIZE + START_WIDTH, j * BLOCK_SIZE + START_HEIGHT, BLOCK_SIZE, BLOCK_SIZE), 1)
    # Running the game
    while not game_over:
        for event in pygame.event.get():
            begin = 0
            if event.type == pygame.QUIT:
                sys.exit()
            font = pygame.font.SysFont("Corbel", 45)
            if event.type == pygame.MOUSEBUTTONDOWN and is_winner == 0:
                begin = 1
                x_coordinate = event.pos[0]
                y_coordinate = event.pos[1]
                print("CLICKED at (" + str(x_coordinate) + ", " + str(y_coordinate) + ") in grid")

                # Check if valid coordinate (if near the grid)
                validPosition = True
                if x_coordinate > (BLOCK_SIZE / 2) + START_WIDTH + (
                        BOARD_WIDTH * BLOCK_SIZE) or x_coordinate < START_WIDTH - (BLOCK_SIZE / 2):
                    validPosition = False
                if y_coordinate > (BLOCK_SIZE / 2) + START_HEIGHT + (
                        BOARD_HEIGHT * BLOCK_SIZE) or y_coordinate < START_HEIGHT - (BLOCK_SIZE / 2):
                    validPosition = False

                # round x-coordinate to closest intersection if difference between coordinates is small
                col = (x_coordinate - START_WIDTH) / BLOCK_SIZE
                row = (y_coordinate - START_HEIGHT) / BLOCK_SIZE
                x_abs_diff = math.fabs(round(row) - row)
                y_abs_diff = math.fabs(round(col) - col)
                if x_abs_diff <= .3:
                    row = round(row)
                if y_abs_diff <= .3:
                    col = round(col)
                if x_abs_diff > .3 or y_abs_diff > .3:
                    validPosition = False

                print("CLICKED at (" + str(row) + ", " + str(col) + ") in array")

                # If array is empty, fill the array and display piece and move to next turn
                if validPosition and gridArr[row][col] == 0:
                    gridArr[row][col] = turn + 1;
                    print(gridArr)

                    # display piece

                    if turn == 0:
                        text_render = font.render("Player 2's Turn", True, MAROON, (0, 0, 0))
                        window.blit(text_render, (212, 10))
                        img = pygame.image.load("White-piece.png")
                        img = pygame.transform.rotozoom(img,0,0.15)
                        img.convert()
                        rect = img.get_rect()
                        rect.center = col * 25 + START_WIDTH, row * 25 + START_HEIGHT
                        window.blit(img, rect)
                        #pygame.draw.circle(window, WHITE, (col * 25 + START_WIDTH, row * 25 + START_HEIGHT), 7)
                    else:
                        text_render = font.render("Player 1's Turn ", True, WHITE, (0, 0, 0))
                        window.blit(text_render, (212, 10))
                        img = pygame.image.load("Maroon-piece.png")
                        img = pygame.transform.rotozoom(img,0,0.17)
                        img.convert()
                        rect = img.get_rect()
                        rect.center = col * 25 + START_WIDTH, row * 25 + START_HEIGHT
                        window.blit(img, rect)
                        #pygame.draw.circle(window, RED, (col * 25 + START_WIDTH, row * 25 + START_HEIGHT), 7)

                    # check if win
                    if isWin(gridArr, turn + 1):
                        print("WINNER is " + str(turn))
                        is_winner = 1
                        # Displaying the winner
                        player_turn = turn + 1
                        font = pygame.font.SysFont("Corbel", 45, True, True)
                        text_render = font.render("Player " + str(player_turn) + " Wins!   ", True, WHITE, (0, 0, 0))
                        window.blit(text_render, (208, 10))
                        break
                    # next turn
                    turn += 1
                    turn = turn % 2

            # Setting buttons for returning and restarting
            b1 = button(window, (245, 430), "Home")
            b2 = button(window, (350,430), "Restart")
            # Respond based on which button user has clicked
            if turn == 0 and begin == 0 and is_winner == 0:
                text_render = font.render("Player 1's Turn ", True, WHITE, (0, 0, 0))
                window.blit(text_render, (212, 10))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    game_over = True
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    humanVsHuman()
        pygame.display.update()


def humanVsAI():
    pass

# create the menu
menu = pygame_menu.Menu('Gomoku', WINDOW_WIDTH, WINDOW_HEIGHT, theme=pygame_menu.themes.THEME_DARK)
menu.add.image('Gomoku-main.png', scale=(.5, .5))
menu.add.label('\nSelect an option:', font_size=20)
menu.add.button('Human vs. Human', humanVsHuman)
menu.add.button('Human vs. AI', humanVsAI)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(window)
