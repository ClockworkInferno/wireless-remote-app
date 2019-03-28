#playback options

import os
import sys

def pause():
    #push pause to system
    print("Pause")
    return 

def fastforward():
    #go the next scene
    print("fastward")
    return 

def rewind():
    #go to previous scene
    print("rewind")
    return 


#main
count = 0

while count == 0:
    choice = int(input("1. Pause \n 2. fastforward \n 3. rewind \n 4. exit playback options \n"))
    print(choice)
    
    if (choice == 1):
        pause()

    if (choice == 2):
        fastforward()

    if (choice == 3):
        rewind()

    if (choice == 4):
        break
