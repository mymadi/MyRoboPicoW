'''
MyRoboPW: Test for 2x RGB LEDs
Date: 1/7/2023
Code by: NAR

Additional Library:
    - neopixel.mpy
'''

import time
import board
import neopixel
import random

# Configure the setup
PIXEL_PIN = board.GP18  # pin that the NeoPixel is connected to
ORDER = neopixel.GRB    # pixel color channel order
COLORB = (0, 0, 255)    # color to blink (Red, Green, Blue)
COLORR = (255, 0, 0)    # color to blink (Red, Green, Blue)
COLORG = (0, 255, 0)    # color to blink (Red, Green, Blue)
CLEAR = (0, 0, 0)       # clear (or second color)
DELAY = 0.5             # blink rate in seconds
num_pixel = 2           # number of RGB LEDs

# Create the NeoPixel object
pixel = neopixel.NeoPixel(PIXEL_PIN, num_pixel, brightness=0.1, pixel_order=ORDER)

while True:
    # Blue Color
    for i in range (num_pixel):
        pixel[i] = COLORB
        time.sleep(DELAY)
        pixel[i] = CLEAR
        time.sleep(DELAY)
    # Red Color
    for j in range(num_pixel):
        pixel[j] = COLORR
        time.sleep(DELAY)
        pixel[j] = CLEAR
        time.sleep(DELAY)
   # Green Color
    for k in range (num_pixel):
        pixel[k] = COLORG
        time.sleep(DELAY)
        pixel[k] = CLEAR
        time.sleep(DELAY)
             
    time.sleep(1)
    
    # Clear the Pixels
    pixel.fill((0, 0, 0))
     
    # Random Color for ALL Pixels
    for i in range (10):
        pixel.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        pixel.show()
        time.sleep(DELAY)

    time.sleep(1)
    
    # Clear the Pixels
    pixel.fill((0, 0, 0))
