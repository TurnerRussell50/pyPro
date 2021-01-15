import time
import board
import pulseio
from adafruit_motor import servo

pwm = pulseio.PWMOut(board.A2, frequency=50)

moto=servo.ContinuousServo(pwm)

moto.ContinuousServo[11].throttle = 1
time.sleep = 1

moto.ContinuousServo[11].throttle = 0
time.sleep = 1

moto.ContinuousServo[11].throttle = -1
time.sleep = 1

moto.ContinuousServo[11].throttle = 0
time.sleep = 1
