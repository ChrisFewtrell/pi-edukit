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

def LeftMotorStop():
    GPIO.output(pinMotorLeftForwards, 0)
    GPIO.output(pinMotorLeftBackwards, 0)
    
def LeftMotorGo(direction):
    GPIO.output(pinMotorLeftForwards, direction)
    GPIO.output(pinMotorLeftBackwards, (not direction))

def RightMotorStop():
    GPIO.output(pinMotorRightForwards, 0)
    GPIO.output(pinMotorRightBackwards, 0)
    
def RightMotorGo(direction):
    GPIO.output(pinMotorRightForwards, direction)
    GPIO.output(pinMotorRightBackwards, (not direction))
    
def StopMotors():
    LeftMotorStop()
    RightMotorStop()

def Forwards():
    LeftMotorGo(True)
    RightMotorGo(True)
    
def Backwards():
    LeftMotorGo(False)
    RightMotorGo(False)

def SpinRight():
    LeftMotorGo(False)
    RightMotorGo(True)

def SpinLeft():
    LeftMotorGo(True)
    RightMotorGo(False)

def Right():
    LeftMotorStop()
    RightMotorGo(True)
    
def Left():
    RightMotorStop()
    MotorLeft(True)



Forwards();
time.sleep(5)



StopMotors()
# time.sleep(1)

# Backwards()
# time.sleep(1)

GPIO.cleanup()

Alice=10
John=9
Grace=8
Toby=7
