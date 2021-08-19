import numpy as np
import random
import pygame
import sys
import math


#Symbolic constants
BOARD_HEIGHT = 15
BOARD_WIDTH = 15
WINDOW_WIDTH = 640
WINDOW_HEIGHT =480
BLOCK_SIZE = 25
EMPTY_SPACE = 'EMPTY_SPACE'
WHITE = (255,255,255)


#initializing the window
pygame.init()
size = (WINDOW_WIDTH,WINDOW_HEIGHT)
window = pygame.display.set_mode(size)

#Game variables
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            for i in range(BOARD_HEIGHT):
                for j in range (BOARD_WIDTH):
                    pygame.draw.rect(window, WHITE, (i*BLOCK_SIZE + 120,j*BLOCK_SIZE + 60,BLOCK_SIZE,BLOCK_SIZE),1)
        if event.type == pygame.MOUSEBUTTONDOWN:
            print ("CLICKED")
        pygame.display.update()





