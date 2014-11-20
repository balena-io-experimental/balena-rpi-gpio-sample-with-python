#!/usr/bin/python

import RPi.GPIO as GPIO
import time
#import logging

#logging.basicConfig(format='%(levelname)s-%(asctime)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG,filename='/App/gpio.log')

# Set GPIO mode: GPIO.BCM or GPIO.BOARD
GPIO.setmode(GPIO.BOARD)

# GPIO pins list based on GPIO.BOARD
gpioList1 = [3,5,7,8,10,11,12,13,15]
gpioList2 = [16,18,19,21,22,23,24,26]

# Set mode for each gpio pin
GPIO.setup(gpioList1, GPIO.OUT)
GPIO.setup(gpioList2, GPIO.OUT)

while True:
	# Change gpio pins in list 1 from low to high and list 2 from high to low
	GPIO.output(gpioList1, 1)
	GPIO.output(gpioList2, 0)
	time.sleep(1)

	# Change gpio pin in list 1 from high to low and list 2 from low to high
	GPIO.output(gpioList1, 0)
	GPIO.output(gpioList2, 1)
	time.sleep(1)

# Reset all gpio pin
GPIO.cleanup()