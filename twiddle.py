#!/usr/bin/env python

import math
import bitmaps
import time
import pygame
import random
import tkinter

def playTwiddle(runState):
    runState[0] = True

    BLACK = (0, 0, 0)
    BLUE = (177, 98, 134)
    DBLUE = (143, 63, 113)

    CMAP = [BLUE]*16

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

    pygame.init()

    WINDOW_SIZE = [WIDTH*4, HEIGHT*4]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    pygame.display.set_caption("Twiddle")

    done = False

    clock = pygame.time.Clock()

    startTime = time.time()
    moves = 0

    while not done:

        CMAP = [BLUE]*16
        # check the area with the least distance
        # ALERT: CENTRE COORDS ARE (X,Y)
        dcal = lambda tup: math.dist(
            [50*i for i in tup],
            pygame.mouse.get_pos()
        )

        cens = [[i,j] for i in range(1,4) for j in range(1,4)]
        cens.sort(key=dcal)
        center = cens[0]

        if pygame.mouse.get_focused():
            CMAP[4*(center[1]-1)+(center[0]-1)] = DBLUE
            CMAP[4*(center[1])+(center[0]-1)] = DBLUE
            CMAP[4*(center[1]-1)+(center[0])] = DBLUE
            CMAP[4*(center[1])+(center[0])] = DBLUE

        center[0], center[1] = center[1], center[0]

        # event processing
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                X = center[1]-1
                Y = center[0]-1
                grid[4*Y+X], grid[4*Y+X+1] = grid[4*Y+X+1], grid[4*Y+X] 
                grid[4*Y+X], grid[4*Y+X+4] = grid[4*Y+X+4], grid[4*Y+X] 
                grid[4*Y+X+4], grid[4*Y+X+5] = grid[4*Y+X+5], grid[4*Y+X+4] 
                moves += 1

        
        # fill colors
        screen.fill(BLACK)
        for y in range(4):
            for x in range(4):
                color = CMAP[ 4*y+x ]
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
        clock.tick(20)

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
        mv = tkinter.Label(infmenu, text=f"Total Moves Taken: {moves}\n")
        mv.pack()
        infmenu.mainloop()

# multiple windows kinda work
if __name__=='__main__':
    rns = [True]
    playTwiddle(rns)
# playTwiddle()
