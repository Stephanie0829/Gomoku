import numpy as np
import random
import pygame
import sys
import math


#Symbolic constants
BOARD_HEIGHT = 14
BOARD_WIDTH = 14
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
START_HEIGHT = 60
START_WIDTH = 120
BLOCK_SIZE = 25
WHITE = (255,255,255)
RED = (255,0,0)


#initializing the window
pygame.init()
size = (WINDOW_WIDTH,WINDOW_HEIGHT)
window = pygame.display.set_mode(size)

#Game variables
game_over = False
turn = 0

# Create grids (Array and GUI)
gridArr = np.zeros((15, 15))
print(gridArr)
for i in range(BOARD_HEIGHT):
    for j in range(BOARD_WIDTH):
        pygame.draw.rect(window, WHITE, (i * BLOCK_SIZE + START_WIDTH, j * BLOCK_SIZE + START_HEIGHT, BLOCK_SIZE, BLOCK_SIZE), 1)


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # if event.type == pygame.MOUSEMOTION:
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_coordinate = event.pos[0]
            y_coordinate = event.pos[1]
            print ("CLICKED at (" + str(x_coordinate) + ", " + str(y_coordinate) + ") in grid")

            # Check if valid coordinate (if near the grid)
            validPosition = True
            if x_coordinate > (BLOCK_SIZE/2) + START_WIDTH + (BOARD_WIDTH*BLOCK_SIZE) or x_coordinate < START_WIDTH - (BLOCK_SIZE/2):
                validPosition = False
            if y_coordinate > (BLOCK_SIZE/2) + START_HEIGHT + (BOARD_HEIGHT*BLOCK_SIZE) or y_coordinate < START_HEIGHT - (BLOCK_SIZE/2):
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
                gridArr[row][col] = 1;
                print(gridArr)
                # display piece
                if turn == 0:
                    pygame.draw.circle(window, WHITE, (x_coordinate,y_coordinate), 7)
                else:
                    pygame.draw.circle(window, RED, (x_coordinate,y_coordinate), 7)
                # next turn
                turn += 1
                turn = turn % 2



        pygame.display.update()
