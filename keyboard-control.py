import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Frequency = 20
Stop = 0

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

pwmMotorRightForwards = GPIO.PWM(pinMotorRightForwards, Frequency)
pwmMotorRightBackwards = GPIO.PWM(pinMotorRightBackwards, Frequency)
pwmMotorLeftForwards = GPIO.PWM(pinMotorLeftForwards, Frequency)
pwmMotorLeftBackwards = GPIO.PWM(pinMotorLeftBackwards, Frequency)

pwmMotorRightForwards.start(Stop)
pwmMotorRightBackwards.start(Stop)
pwmMotorLeftForwards.start(Stop)
pwmMotorLeftBackwards.start(Stop)

def LeftMotorStop():
    pwmMotorLeftForwards.ChangeDutyCycle(Stop)
    pwmMotorLeftBackwards.ChangeDutyCycle(Stop)
    
def LeftMotorGo(direction, dutyCycle):
    if direction:
        pwmMotorLeftForwards.ChangeDutyCycle(dutyCycle)
        pwmMotorLeftBackwards.ChangeDutyCycle(Stop)
    else:
        pwmMotorLeftForwards.ChangeDutyCycle(Stop)
        pwmMotorLeftBackwards.ChangeDutyCycle(dutyCycle)

def RightMotorStop():
    pwmMotorRightForwards.ChangeDutyCycle(Stop)
    pwmMotorRightBackwards.ChangeDutyCycle(Stop)
    
def RightMotorGo(direction, dutyCycle):
    if direction:
        pwmMotorRightForwards.ChangeDutyCycle(dutyCycle)
        pwmMotorRightBackwards.ChangeDutyCycle(Stop)
    else:
        pwmMotorRightForwards.ChangeDutyCycle(Stop)
        pwmMotorRightBackwards.ChangeDutyCycle(dutyCycle)

    
def StopMotors():
    LeftMotorStop()
    RightMotorStop()

def Forwards(speed):
    LeftMotorGo(True, speed)
    RightMotorGo(True, speed)
    
def Backwards(speed):
    LeftMotorGo(False, speed)
    RightMotorGo(False, speed)

def SpinLeft(speed):
    LeftMotorGo(False, speed)
    RightMotorGo(True, speed)

def SpinRight(speed):
    LeftMotorGo(True, speed)
    RightMotorGo(False, speed)

def Left(speed):
    LeftMotorStop()
    RightMotorGo(True, speed)
    
def Right(speed):
    RightMotorStop()
    LeftMotorGo(True, speed)

import sys, termios, tty, os


def getch():
  import sys, tty, termios
  old_settings = termios.tcgetattr(0)
  new_settings = old_settings[:]
  new_settings[3] &= ~termios.ICANON
  try:
    termios.tcsetattr(0, termios.TCSANOW, new_settings)
    ch = sys.stdin.read(1)
  finally:
    termios.tcsetattr(0, termios.TCSANOW, old_settings)
  return ch

speed = 100

while True:
    char = getch()

    if (char == "q"):
        StopMotors()
        print("Quitting")
        exit(0)  

    if (char == " "):
        print('STOP')
        StopMotors()

    if (char == "a"):
        print('Left pressed')
        SpinLeft(speed)

    if (char == "d"):
        print('Right pressed')
        SpinRight(speed)

    elif (char == "w"):
        print('Up pressed') 
        Forwards(speed)       
    
    elif (char == "s"):
        print('Down pressed')
        Backwards(speed)
