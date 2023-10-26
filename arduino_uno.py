"""
Created by: Youngwook Go
Created on: OCT 2023
Checks distances with sonar sensor.
"""

import time
import board
import adafruit_hcsr04
import pwmio
from adafruit_motor import servo

# setup
pwm = pwmio.PWMOut(board.GP3, frequency=50)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP1, echo_pin=board.GP2)

my_servo = servo.ContinuousServo(pwm)

while True:
    try:
        print("Distance: " + str(sonar.distance))
        if sonar.distance < 50:
            my_servo.throttle = 1.0
            print("90")

        else:
            my_servo.throttle = 0
            print("0")
            
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)