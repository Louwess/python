import RPi.GPIO as GPIO
import time

# Pin Definitons:
ledPin = 18 # Broadcom pin 18

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output

GPIO.output(ledPin, GPIO.LOW)
print("low")
time.sleep(0.5)
GPIO.output(ledPin, GPIO.HIGH)
print("high")
time.sleep(0.5)
