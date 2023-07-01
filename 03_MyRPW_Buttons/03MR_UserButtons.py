"""
MyRobo: Test for 2x User Buttons
Date: 1/7/2023
Code by: NAR

"""

import time
import board
import digitalio



pb20 = digitalio.DigitalInOut(board.GP20)
pb20.direction = digitalio.Direction.INPUT

pb21 = digitalio.DigitalInOut(board.GP21)
pb21.direction = digitalio.Direction.INPUT

LED = [0,0,0,0,0,0,0,0,0,0,0,0,0]
LEDS = (board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,board.GP5,board.GP16,board.GP17,board.GP6,board.GP26,board.GP27,board.GP7,board.GP28)

for i in range(13):
    LED[i] = digitalio.DigitalInOut(LEDS[i])
    LED[i].direction = digitalio.Direction.OUTPUT
    
while True:
    if pb20.value == False:
        for j in range(0,6):
            LED[j].value = True
            time.sleep(0.1)
        time.sleep(0.5)
        for j in range(0,6):
            LED[j].value = False
            time.sleep(0.1)
    elif pb21.value == False:    
        for j in range(7,13):
            LED[j].value = True
            time.sleep(0.1)
        time.sleep(0.5)
        for j in range(7,13):
            LED[j].value = False
            time.sleep(0.1)
    else:
        pass
