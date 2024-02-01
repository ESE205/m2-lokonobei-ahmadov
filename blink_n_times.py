import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep from time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

LED_PIN = 11

GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)   

# number of blinks
n = int(input("n: ") or 5)

blink_count = 0

while blink_count < n:
   GPIO.output(LED_PIN, GPIO.HIGH) # Turn on
   sleep(1)                        # Sleep for 1 second
   GPIO.output(LED_PIN, GPIO.LOW)  # Turn off
   sleep(1)                        # Sleep for 1 second
   blink_count += 1

GPIO.cleanup()
