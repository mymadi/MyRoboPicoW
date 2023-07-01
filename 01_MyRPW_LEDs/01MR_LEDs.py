'''
MyRobo: Test for 13x GPIO LEDs
Date: 1/7/2023
Code by: NAR

'''
import board
import digitalio
import time


LED = [0,0,0,0,0,0,0,0,0,0,0,0,0]
LEDS = (board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,board.GP5,board.GP16,board.GP17,board.GP6,board.GP26,board.GP27,board.GP7,board.GP28)

for i in range(13):
    LED[i] = digitalio.DigitalInOut(LEDS[i])
    LED[i].direction = digitalio.Direction.OUTPUT
    

while True:
    for j in range(13):
        LED[j].value = True
        time.sleep(0.1)
        
    for j in range(13):
        LED[j].value = False
        time.sleep(0.1)
