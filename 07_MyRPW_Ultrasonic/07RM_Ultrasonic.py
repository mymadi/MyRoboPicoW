'''
MyRoboPW: 3V-5.5V SR04P Ultrasonic Ranging Module
Date: 2/7/2023
Code by: NAR

Additional Library:
    - adafruit_hcsr04.mpy
'''

import time
import board
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP5, echo_pin=board.GP4)


while True:
    try:
        print(sonar.distance)
    except RuntimeError:
        print("Retrying!")
        pass
    time.sleep(0.1)
