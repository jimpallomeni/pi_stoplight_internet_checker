import os
import RPi.GPIO as GPIO ## Import GPIO library
import time

# Written by John Impallomeni
# May 14, 2016
# Version 1.0
# Is the internet up redlight


GPIO.cleanup() 

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(16, GPIO.OUT) ## Setup GPIO Pin 16 to OUT as Red
GPIO.setup(18, GPIO.OUT) ## Setup GPIO Pin 18 to OUT as Yellow
GPIO.setup(22, GPIO.OUT) ## Setup GPIO Pin 7 to OUT as Green

# Network Stuff

hostname = "google.com"
response = 1
reset = 0

# Shutdown all ports
GPIO.output(22,False)## Switch Green Off
GPIO.output(18,False)## Switch Yellow Off
GPIO.output(16,False)## Switch Red Off


# Light Functions
def red_light():
    GPIO.output(18,False)## Switch Yellow Off
    GPIO.output(22,False)## Switch Green Off
    GPIO.output(16,True)## Red On


def green_light():
    GPIO.output(18,False)## Switch Yellow Off
    GPIO.output(16,False)## Switch Red Off
    GPIO.output(22,True)## Green On


def yellow_light():
    GPIO.output(22,False)## Switch Green Off
    GPIO.output(16,False)## Switch Red Off
    GPIO.output(18,True)## Yellow On


while True:
    response = os.system("ping -c 1 " + hostname)
    print(response)
    if response == 0:
        green_light()
        time.sleep(5)
        reset = 0
    elif response != 0:
        if reset < 30:
            reset += 1
            time.sleep(1)
            yellow_light()
        else:
            red_light()
            time.sleep(1)
