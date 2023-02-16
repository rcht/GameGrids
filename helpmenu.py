#!/usr/bin/env python

from tkinter import *

def help():

    helpmenu = Tk()

    helpmenu.title("GameGrids Help")

    helpstr = '''
    Welcome to GameGrids!

    This is a collection of fun puzzle games which also challenge you mentally. 

    Here's a brief overview of all of them.

    ColorSwitch: By clicking on a square, all of its neighbours (including diagonals) have their colors flipped. Your goal is to make all of the colors equal.

    Fifteen Puzzle: A classic puzzle in which you slide pieces through an empty square to arrange the numbers in order. Use arrow keys to control.

    Twiddle: Arrange the numbers in order by rotating 2x2 blocks of squares in a grid. The game will highlight the block your mouse is on, and you can click to rotate it.
    '''

    title = Label(helpmenu,text=helpstr)
    title.pack()

    helpmenu.mainloop()
