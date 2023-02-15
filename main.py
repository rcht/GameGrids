#!/usr/bin/env python

import fifteen
import colorswitch

print("1 -> ColorSwitch")
print("2 -> Fifteen Puzzle")

while True:
    try:
        inp = int(input("Play a game? ").strip())
    except:
        print("Invalid input. Ending.")
        break
    if inp==1:
        colorswitch.playColorSwitch()
    elif inp==2:
        fifteen.playFifteen()
