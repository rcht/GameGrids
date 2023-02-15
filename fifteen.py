#!/usr/bin/env python

import bitmaps
import time
import pygame
import random

def playFifteen():

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    CMAP = [ RED, RED, RED, RED, 
             RED, GREEN, GREEN, GREEN,
             RED, GREEN, BLUE, BLUE,
             RED, GREEN, BLUE, BLACK]

    WIDTH = 50
    HEIGHT = 50

    def valid(x, y):
        if x<0 or y<0 or x>=4 or y>=4:
            return False
        else:
            return True

    grid = []
    for row in range(4):
        for column in range(4):
            grid.append( row*4 + column + 1 )  
    random.shuffle(grid)
    # print(grid)
    pygame.init()

    WINDOW_SIZE = [WIDTH*4, HEIGHT*4]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    pygame.display.set_caption("Fifteen Puzzle")

    done = False

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // WIDTH
                row = pos[1] // HEIGHT

        
        # fill colors
        screen.fill(BLACK)
        for y in range(4):
            for x in range(4):
                color = CMAP[ grid[4*y+x] - 1 ]
                pygame.draw.rect(screen,
                                 color,
                                 [ WIDTH * x,
                                   HEIGHT * y,
                                   WIDTH,
                                   HEIGHT])
                bmp = [i for i in bitmaps.bitmap[ grid[4*y+x] ]]
                for i in range( HEIGHT ):
                    for j in range( WIDTH ):
                        if bmp[i][j]:
                            screen.set_at( ( WIDTH*x + j, HEIGHT*y + i  ), BLACK ) 

        pygame.display.flip()
        time.sleep(2)
        done = True
        # clock.tick(60)
    pygame.quit()

# multiple windows kinda work
playFifteen()
# playFifteen()
