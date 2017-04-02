# CamJam EduKit 3 - Robotics
# Worksheet 6 – Measuring Distance
##############################################################
import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library
# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Define GPIO pins to use on the Pi
pinTrigger = 17
pinEcho = 18

speedOfSoundInCmPerS = 34300 / 2

print("Hunting")

# Set pins as output and input
GPIO.setup(pinTrigger, GPIO.OUT) # Trigger
GPIO.setup(pinEcho, GPIO.IN) # Echo

def WaitWhileEchoIs(echoState):
    WaitCount = 0
    TimeStart = time.time()
    while GPIO.input(pinEcho)==echoState:
        WaitCount = WaitCount + 1
        if time.time() - TimeStart > 0.2:
            print("timed out")
            return 0.2
                
    if WaitCount == 0:
        return 0
    
    return time.time() - TimeStart

def WaitForEchoLow():
    return WaitWhileEchoIs(1)

def WaitForEchoHigh():
    return WaitWhileEchoIs(0)

def SendPulse(duration):
    GPIO.output(pinTrigger, True)
    time.sleep(duration)
    GPIO.output(pinTrigger, False)

def GetDistance():
    # Send 10us pulse to trigger
    pulseSent = time.time()
    SendPulse(0.00001)
    
    WaitForEchoHigh()
    WaitForEchoLow()
    difference = time.time() - pulseSent

    x = difference * speedOfSoundInCmPerS
    correctedDistance = 1.0216 * x - 10.768

    return correctedDistance

def Settle(sleepTime):
    # Set trigger to False (Low)
    GPIO.output(pinTrigger, False)

    # Allow module to settle
    time.sleep(sleepTime)


######################################################################

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
    dutyCycle = dutyCycle * 1.1
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

def SpinLeftFor(speed, spinTime):
    LeftMotorGo(True, speed)
    RightMotorGo(False, speed)
    time.sleep(spinTime)

def SpinRightFor(speed, spinTime):
    LeftMotorGo(False, speed)
    RightMotorGo(True, speed)
    time.sleep(spinTime)
    
######################################################################

distancePrintCounter = 0
def GetDistanceWithPrint():
    global distancePrintCounter
    distance = GetDistance()

    distancePrintCounter += 1
    if distancePrintCounter == 200:
        print("Distance: {:8.5f}".format(distance))
        distancePrintCounter = 0
    return distance


turnRight = False
def StartTurning(speed):
    global turnRight

    if turnRight:
        print("Turning Right")
        SpinRight(speed)
        turnRight = False
    else:
        print("Turning left")
        SpinLeft(speed)
        turnRight = True

def TurnUntilClear(speed):
    global stopDistance
    turnTime = 3
    safeDistance = 3 *stopDistance
    
    distance = GetDistanceWithPrint()
    if distance > safeDistance:
        print("Looks safe!")
        return
    
    timeStartingTurn = time.time()
    StartTurning(speed)
    
    while time.time() - timeStartingTurn < turnTime:
        distance = GetDistanceWithPrint()
           
        if distance > safeDistance:
            print("Looks safe!")
            return

    print("Still not clear! Let's turn the other way!")
    TurnUntilClear(speed)

        
            
stopDistance = 20

speed = 80

print("Starting")
Settle(0.01)
distance = GetDistanceWithPrint()



Forwards(speed)
try:
    # Repeat the next indented block forever
    while True:
        distance = GetDistanceWithPrint()

        # Keep moving forwards until we get near to something
        while distance > stopDistance:
             distance = GetDistanceWithPrint()

        print("Too close - trying to get around")
        TurnUntilClear(speed)
        
        print("OK - let's go")
        Forwards(speed)
        
# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    # Reset GPIO settings
    GPIO.cleanup()
