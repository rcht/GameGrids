#!/usr/bin/env python

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import fifteen
import colorswitch
import twiddle
import tkinter
import helpmenu

runstate = [False]

def playcs():
    colorswitch.playColorSwitch(runstate)

def playfif():
    fifteen.playFifteen(runstate)

def playtwd():
    twiddle.playTwiddle(runstate)

root = tkinter.Tk()
root.title("Rachit's GameGrids")

ttl = tkinter.Label(root, text="Welcome to GameGrids!\n\nOptions:\n")
ttl.pack()


btn1 = tkinter.Button(root, text='Play ColorSwitch', command=playcs,width=30)
btn1.pack()

btn2 = tkinter.Button(root, text='Play Fifteen Puzzle', command=playfif, width=30)
btn2.pack()

btn3 = tkinter.Button(root, text='Play Twiddle', command=playtwd, width=30)
btn3.pack()

btn4 = tkinter.Button(root, text='Help', command=helpmenu.help, width=30)
btn4.pack()

credit = tkinter.Label(root, text="\n\nMade by Rachit Arora (2022384)")
credit.pack()

root.mainloop()
