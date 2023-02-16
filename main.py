#!/usr/bin/env python

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import fifteen
import colorswitch

print("1 -> ColorSwitch")
print("2 -> Fifteen Puzzle")
print()

while True:
    try:
        inp = int(input("Play a game? ").strip())
    except:
        print("Invalid input. Ending.")
        break
    print()
    if inp==1:
        colorswitch.playColorSwitch()
    elif inp==2:
        fifteen.playFifteen()
