import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# SpinRight motor forwards 10, backwards 9

# SpinLeft motor forwards 8, backwards 7
pinMotorRightForwards = 9
pinMotorRightBackwards = 10
pinMotorLeftForwards = 8
pinMotorLeftBackwards = 7

GPIO.setup(pinMotorRightForwards, GPIO.OUT)
GPIO.setup(pinMotorRightBackwards, GPIO.OUT)
GPIO.setup(pinMotorLeftForwards, GPIO.OUT)
GPIO.setup(pinMotorLeftBackwards, GPIO.OUT)

def StopMotors():
    GPIO.output(pinMotorRightForwards, 0)
    GPIO.output(pinMotorRightBackwards, 0)
    GPIO.output(pinMotorLeftForwards, 0)
    GPIO.output(pinMotorLeftBackwards, 0)

def Forwards():
    GPIO.output(pinMotorRightForwards, 1)
    GPIO.output(pinMotorRightBackwards, 0)
    GPIO.output(pinMotorLeftForwards, 1)
    GPIO.output(pinMotorLeftBackwards, 0)

def Backwards():
    GPIO.output(pinMotorRightForwards, 0)
    GPIO.output(pinMotorRightBackwards, 1)
    GPIO.output(pinMotorLeftForwards, 0)
    GPIO.output(pinMotorLeftBackwards, 1)

def SpinRight():
    GPIO.output(pinMotorRightForwards, 1)
    GPIO.output(pinMotorRightBackwards, 0)
    GPIO.output(pinMotorLeftForwards, 0)
    GPIO.output(pinMotorLeftBackwards, 1)

def SpinLeft():
    GPIO.output(pinMotorRightForwards, 0)
    GPIO.output(pinMotorRightBackwards, 1)
    GPIO.output(pinMotorLeftForwards, 1)
    GPIO.output(pinMotorLeftBackwards, 0)

def Right():
    GPIO.output(pinMotorRightForwards, 1)
    GPIO.output(pinMotorRightBackwards, 0)
    GPIO.output(pinMotorLeftForwards, 0)
    GPIO.output(pinMotorLeftBackwards, 0)

def Left():
    GPIO.output(pinMotorRightForwards, 0)
    GPIO.output(pinMotorRightBackwards, 0)
    GPIO.output(pinMotorLeftForwards, 1)
    GPIO.output(pinMotorLeftBackwards, 0)
    
Forwards()
time.sleep(1.5)


StopMotors()
# time.sleep(1)

# Backwards()
# time.sleep(1)

GPIO.cleanup()

Alice=10
John=9
Grace=8
Toby=7
