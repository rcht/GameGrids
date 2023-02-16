#!/usr/bin/env python

import time
import random
import pygame
import tkinter

def playColorSwitch(runState):

    runState[0] = True

    BLACK = (0, 0, 0)
    WHITE = (255, 0, 0)
    GREEN = (0, 255, 0)

    WIDTH = 40
    HEIGHT = 40
    MARGIN = 5

    NUM = 4

    def valid(x, y):
        if x<0 or y<0 or x>=NUM or y>=NUM:
            return False
        else:
            return True

    grid = []
    for row in range(NUM):
        grid.append([])
        for column in range(NUM):
            grid[row].append(random.randint(0,1))  
    pygame.init()

    SQ_SIDE = WIDTH*(NUM) + MARGIN*(NUM+1)
    WINDOW_SIZE = [SQ_SIDE, SQ_SIDE]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    pygame.display.set_caption("ColorSwitch")

    done = False
    allDone = False

    clock = pygame.time.Clock()
    startTime = time.time()
    moves = 0

    while not done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True 
                allDone = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                moves += 1
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        if valid(row + i, column + j):
                            grid[row+i][column+j] = 1- grid[row+i][column+j]
        screen.fill(BLACK)
        for row in range(NUM):
            for column in range(NUM):
                if grid[row][column] == 1:
                    color = WHITE
                elif grid[row][column]==0:
                    color = GREEN
                pygame.draw.rect(screen,
                                 color,
                                 [ (MARGIN+WIDTH) * column + MARGIN,
                                  (MARGIN+HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

        clock.tick(60)
        pygame.display.flip()
        
        prev = grid[0][0]
        allEq = True
        for i in range(NUM):
            for j in range(NUM):
                if grid[i][j] != prev:
                    allEq = False
                prev = grid[i][j]

        if allEq:
            done = True



    runState[0] = False
    pygame.quit()

    if allEq:
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
    playColorSwitch(rns)


