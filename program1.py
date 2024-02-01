import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
from time import sleep   # Import the sleep from the time module
GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering 

switch_pin = 8 
led_pin = 11

GPIO.setup(switch_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)

while True:
   if GPIO.input(switch_pin) == GPIO.HIGH:
      GPIO.output(led_pin, GPIO.HIGH)
   else:
      GPIO.output(led_pin, GPIO.LOW)

GPIO.cleanup()
