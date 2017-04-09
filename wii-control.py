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

pinBuzzer = 21
pinBigLed = 26
pinYellowLed = 19

GPIO.setup(pinMotorRightForwards, GPIO.OUT)
GPIO.setup(pinMotorRightBackwards, GPIO.OUT)
GPIO.setup(pinMotorLeftForwards, GPIO.OUT)
GPIO.setup(pinMotorLeftBackwards, GPIO.OUT)

GPIO.setup(pinBuzzer, GPIO.OUT)
GPIO.setup(pinBigLed, GPIO.OUT)
GPIO.setup(pinYellowLed, GPIO.OUT)

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


import cwiid, time, math

button_delay = 0.1

print('Please press buttons 1 + 2 on your Wiimote now ...')
time.sleep(1)

# This code attempts to connect to your Wiimote and if it fails the program quits
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Cannot connect to your Wiimote. Run again and make sure you are holding buttons 1 + 2!"
  quit()

print('Connected')

wii.rpt_mode = cwiid.RPT_BTN

speed = 100

while True:
    buttons = wii.state['buttons']

    # Detects whether + and - are held down and if they are it quits the program
    if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
        print
        '\nClosing connection ...'
        # NOTE: This is how you RUMBLE the Wiimote
        wii.rumble = 1
        time.sleep(1)
        wii.rumble = 0
        exit(wii)

    elif (buttons & cwiid.BTN_LEFT):
        print 'Left pressed'
        SpinLeft(speed)
        time.sleep(button_delay)

    elif (buttons & cwiid.BTN_RIGHT):
        print('Right pressed')
        SpinRight(speed)
        time.sleep(button_delay)

    elif (buttons & cwiid.BTN_UP):
        print('Up pressed')
        Forwards(speed)
        time.sleep(button_delay)

    elif (buttons & cwiid.BTN_DOWN):
        print('Down pressed')
        Backwards(speed)
        time.sleep(button_delay)
    else:
        StopMotors()

    if (buttons & cwiid.BTN_MINUS):
        speed = speed - 5
        print ('Minus Button pressed:' , speed)

        time.sleep(button_delay)

    if (buttons & cwiid.BTN_PLUS):
        speed = speed + 5
        print('Plus Button pressed: ', speed)
        time.sleep(button_delay)


    if (buttons & cwiid.BTN_HOME):
        print('Speeed = ', speed)
        time.sleep(button_delay)

    speed = min(speed, 100)
    speed = max(speed, 0)

    if (buttons & cwiid.BTN_B):
        GPIO.output(pinBuzzer, True)
        GPIO.output(pinBigLed, True)
    else:
        GPIO.output(pinBuzzer, False)
        GPIO.output(pinBigLed, False)

    if (buttons & cwiid.BTN_A):
        GPIO.output(pinYellowLed, True)
    else:
        GPIO.output(pinYellowLed, False)

