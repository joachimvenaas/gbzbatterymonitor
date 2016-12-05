#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from time import localtime, strftime
import array
import os
import math

from config import *
from mcp3008 import *

ret = 0

print("Batteries high voltage:       " + str(VHIGHBAT))
print("Batteries low voltage:        " + str(VLOWBAT))
print("Batteries dangerous voltage:  " + str(VDNGBAT))
print("ADC high voltage value:       " + str(ADCHIGH))
print("ADC low voltage value:        " + str(ADCLOW))
print("ADC dangerous voltage value:  " + str(ADCDNG))
print(" ")
print("Time	ADC	Volt")
while True:
    ret1 = readadc(ADCCHANNEL, SPICLK, SPIMOSI, SPIMISO, SPICS)
    time.sleep(3)
    ret2 = readadc(ADCCHANNEL, SPICLK, SPIMOSI, SPIMISO, SPICS)
    time.sleep(3)
    ret3 = readadc(ADCCHANNEL, SPICLK, SPIMOSI, SPIMISO, SPICS)
    ret = ret1 + ret2 + ret3
    ret = ret/3
    print(strftime("%H:%M", localtime()) + "	" + str(ret) + "	" + str((ADCVREF / 1024.0) * ret) + "V")
        
    time.sleep(1)
