import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep
import time
import sys
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

#DEBUG = False
#if '-debug' in sys.argv:
#   DEBUG = True

SWITCH_PIN = 8
LED_PIN = 11

GPIO.setup(SWITCH_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

# Input the Blink Rate in seconds
blinkRate = int(input("blink rate (sec): "))
# Input the length of time the program will run in seconds
runTime = int(input("run time (sec): "))

# with open('data.txt', 'w') as data:

runCount = 0
# Turn on LED if switch is on (GPIO.HIGH), turn off (GPIO.LOW) if it is off
while runCount < runTime:
   if GPIO.input(SWITCH_PIN) == GPIO.HIGH:
      GPIO.output(LED_PIN, GPIO.HIGH)
      GPIO.output(LED_PIN, LED_IS_ON)
      sleep(blinkRate)
      runCount += 1
      GPIO.output(LED_PIN, GPIO.LOW)
      sleep(blinkRate)
      runCount += 1
   else:
      sleep(blinkRate)


   #GPIO.output(LED_PIN, LED_IS_ON)
   #data.write(f'{time.time():1.0f} {LED_IS_ON}\n')

   #if DEBUG:
    #  print(f'current time: {time.time():1.0f}' 'iterations: {runCount}' 'LED is on: {LED_IS_ON}')
    #  LED_IS_ON = not(LED_IS_ON)
    #  time.sleep(1)

GPIO.cleanup()
