#!/usr/bin/env python

import bitmaps
import time
import pygame
import random
import tkinter

def playFifteen(runState):

    runState[0] = True

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

    # parity check
    while True:
        inv = 0
        dummygrid = [i for i in grid]
        for i in range(16):
            for j in range(i):
                if (dummygrid[i]%16)*(dummygrid[j]%16) and dummygrid[i]<dummygrid[j]:
                    inv += 1
        zeroPos = dummygrid.index(16)
        posPar = (zeroPos//4)%2

        # print(posPar)
        # print(inv)
        if (posPar + inv) % 2 == 1:
            break
        random.shuffle(grid)
        # break

    pygame.init()

    WINDOW_SIZE = [WIDTH*4, HEIGHT*4]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    pygame.display.set_caption("Fifteen Puzzle")

    done = False

    clock = pygame.time.Clock()

    startTime = time.time()
    moveCount = 0

    while not done:

        holePos = grid.index(16)
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if holePos % 4 != 3:
                        grid[holePos] = grid[holePos+1]
                        grid[holePos+1] = 16
                        holePos += 1
                        moveCount += 1
                if event.key == pygame.K_RIGHT:
                    if holePos % 4:
                        grid[holePos] = grid[holePos-1]
                        grid[holePos-1] = 16
                        holePos -= 1
                        moveCount += 1
                if event.key == pygame.K_UP:
                    if holePos//4 != 3:
                        grid[holePos] = grid[holePos+4]
                        grid[holePos+4] = 16
                        holePos += 4
                        moveCount += 1
                if event.key == pygame.K_DOWN:
                    if holePos//4:
                        grid[holePos] = grid[holePos-4]
                        grid[holePos-4] = 16
                        holePos -= 4
                        moveCount += 1

        
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
        clock.tick(10)

        std = True
        for i in range(1,16):
            if grid[i]<grid[i-1]:
                std = False
        if std:
            done = True

        
    runState[0] = False
    pygame.quit()

    if std:
        infmenu = tkinter.Tk()
        slv = tkinter.Label(infmenu,text="Congrats! Solved!\n")
        slv.pack()
        tm = tkinter.Label(infmenu, text=f"Total Time Taken: {round(time.time()-startTime,2)} seconds\n")
        tm.pack()
        mv = tkinter.Label(infmenu, text=f"Total Moves Taken: {moveCount}\n")
        mv.pack()
        infmenu.mainloop()

# multiple windows kinda work
if __name__=='__main__':
    rns = [True]
    playFifteen(rns)
# playFifteen()
