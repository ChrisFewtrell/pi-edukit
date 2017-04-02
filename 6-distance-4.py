# CamJam EduKit 3 - Robotics
# Worksheet 6 – Measuring Distance
import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library
# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Define GPIO pins to use on the Pi
pinTrigger = 17
pinEcho = 18

speedOfSoundInCmPerS = 34300 / 2

print("Ultrasonic Measurement")

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
    
    timeTillHigh = WaitForEchoHigh()
    timeTillLow = WaitForEchoLow()
    difference = time.time() - pulseSent

    x = difference * speedOfSoundInCmPerS
    correctedDistance = 1.0216 * x - 10.768

    return correctedDistance

def Settle():
    # Set trigger to False (Low)
    GPIO.output(pinTrigger, False)

    # Allow module to settle
    time.sleep(0.01)
    
try:
    # Repeat the next indented block forever
    while True:
         Settle()

         distance = GetDistance()
         print("{:8.5f}".format(distance))

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    # Reset GPIO settings
    GPIO.cleanup()
