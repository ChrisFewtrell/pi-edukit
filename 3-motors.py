import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

GPIO.output(7, 0)
GPIO.output(8, 0)
GPIO.output(9, 0)
GPIO.output(10, 0)

# Turn right motr forwards
GPIO.output(9, 0)
GPIO.output(10, 1)

# Turn left  motor forwards
GPIO.output(7, 0)
GPIO.output(8, 1)

time.sleep(1)

GPIO.cleanup()
