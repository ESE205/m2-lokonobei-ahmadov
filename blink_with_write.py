import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep
import time
import sys
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

DEBUG = False
if '-debug' in sys.argv:
   DEBUG = True

SWITCH_PIN = 8
LED_PIN = 11
LED_IS_ON = False

GPIO.setup(SWITCH_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

# Input the Blink Rate in seconds
blinkRate = int(input("blink rate (sec): "))
# Input the Run Time in seconds
runTime = int(input("run time (sec): "))

startTime1 = int(time.time())
startTime2 = int(time.time())
runcount = 0
# Turn on LED if switch is on (GPIO.HIGH), turn off (GPIO.LOW) if it is off
with open ('data.txt', 'w') as data:
   while startTime1 - runTime < startTime2:
      if GPIO.input(SWITCH_PIN) == GPIO.HIGH:
         GPIO.output(LED_PIN, GPIO.HIGH)
         #with open('data.txt', 'w') as data:
         GPIO.output(LED_PIN, LED_IS_ON)
         data.write(f'{time.time():1.0f} {LED_IS_ON}\n')
         if DEBUG:
            print(f'current time: {time.time():1.0f} iterations: {runcount} LED is ON: {LED_IS_ON}')
         LED_IS_ON = not(LED_IS_ON)
         sleep(1)
         startTime1 += 1
         GPIO.output(LED_PIN, GPIO.LOW)
         #with open('data.txt', 'w') as data:
         GPIO.output(LED_PIN, not(LED_IS_ON))
         data.write(f'{time.time():1.0f} {LED_IS_ON}\n')
         if DEBUG:
            print(f'current time: {time.time():1.0f} iterations: {runcount} LED is ON: {LED_IS_ON}')
         sleep(blinkRate)
         startTime1 += blinkRate
      else:
         sleep(blinkRate)
      runcount += 1

GPIO.cleanup()
