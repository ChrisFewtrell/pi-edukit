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

def SpinRight(speed):
    LeftMotorGo(False, speed)
    RightMotorGo(True, speed)

def SpinLeft(speed):
    LeftMotorGo(True, speed)
    RightMotorGo(False, speed)

def Right(speed):
    LeftMotorStop()
    RightMotorGo(True, speed)
    
def Left(speed):
    RightMotorStop()
    MotorLeft(True, speed)



Forwards(20);
time.sleep(1)
Forwards(40);

time.sleep(1)
Forwards(70);

time.sleep(1)
Forwards(90);

time.sleep(1)
Forwards(100);

time.sleep(1)

StopMotors()
# time.sleep(1)

# Backwards()
# time.sleep(1)

GPIO.cleanup()

Alice=10
John=9
Grace=8
Toby=7
