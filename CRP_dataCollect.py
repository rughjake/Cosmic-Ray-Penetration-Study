#!/usr/bin/env python3
import os
import sys

import RPi.GPIO as GPIO
import time
import datetime

#Detect signals on GPIO on pin 11.
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)

file = "CRPdata9.txt"
data = open(file, "w+")

NCount = 0
deadtime = 0
startdate = datetime.datetime.now()
data.write(str(startdate) + "\n")
starttime = time.time()

try:
    while NCount < 100:
        if GPIO.input(11)==1:
            NCount += 1
            t = time.time() - starttime
            deadtime += 0.1
	    data.write(str(NCount) + ": " + str(t) + "\n")
            print('Hit ' + str(NCount) + ": " + str(t))
            time.sleep(0.1)
finally:
    time_diff = time.time() - starttime
    livetime = time_diff - deadtime
    data.write("Total count = " + str(NCount) + "\n")
    data.write("Count rate = " + str(NCount/time_diff) + " Hz\n")
    data.write("Total dead time = " + str(deadtime) + " seconds\n")
    print('')
    print("Total count =" + str(NCount) + "\n")
    print("Count rate =" + str(NCount/time_diff) + "Hz\n")
    GPIO.cleanup()
