#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import array
import os
import signal
import subprocess
import math
from subprocess import check_output

import threading
import socket

from config import *
from mcp3008 import *

warning = 0
ret = 0
status = 0

# Roundup to nearest 10
def roundup(x):
    return int(math.ceil(x / 10.0)) * 10

# Called on process interruption. Set all pins to "Input" default mode.
def endProcess(signalnum = None, handler = None):
    GPIO.cleanup()
    os.system("sudo killall pngview");
    exit(0)

# Put pins to out mode and low state.
def initPins():
    GPIO.setup(GOODVOLTPIN, GPIO.OUT)
    GPIO.setup(LOWVOLTPIN, GPIO.OUT)
    GPIO.output(GOODVOLTPIN, GPIO.LOW)
    GPIO.output(LOWVOLTPIN, GPIO.LOW)

### Main part

if DEBUGMSG == 1:
    print("Batteries high voltage:       " + str(VHIGHBAT))
    print("Batteries low voltage:        " + str(VLOWBAT))
    print("Batteries dangerous voltage:  " + str(VDNGBAT))
    print("ADC high voltage value:       " + str(ADCHIGH))
    print("ADC low voltage value:        " + str(ADCLOW))
    print("ADC dangerous voltage value:  " + str(ADCDNG))

# Prepare handlers for process exit
signal.signal(signal.SIGTERM, endProcess)
signal.signal(signal.SIGINT, endProcess)

# Use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# Init output pins
initPins()

batterystatus = 0
os.system(PNGVIEWPATH + "/pngview -b 0 -l 299999 -x 650 -y 5 " + ICONPATH + "/battery50.png &")


while True:
    i = 0
    killid = 0

    # Read ADC measure on channel ADCCHANNEL
    ret1 = readadc(ADCCHANNEL, SPICLK, SPIMOSI, SPIMISO, SPICS)
    time.sleep(3)
    ret2 = readadc(ADCCHANNEL, SPICLK, SPIMOSI, SPIMISO, SPICS)
    time.sleep(3)
    ret3 = readadc(ADCCHANNEL, SPICLK, SPIMOSI, SPIMISO, SPICS)
    ret = ret1 + ret2 + ret3
    ret = ret/3

    if DEBUGMSG == 1:
      print("ADC value: " + str(ret) + " (" + str((3.3 / 1024.0) * ret) + " V)")
 
    if ret < ADCDNG:
        # Dangerous battery voltage: Shutdown
        if status != 0:
            os.system(PNGVIEWPATH + "/pngview -b 0 -l 300000 -x 650 -y 5 " + ICONPATH + "/battery0.png &")
            if DEBUGMSG == 1:
                print("Changed battery icon to 0")
            out = check_output("ps aux | grep pngview | awk '{ print $2 }'", shell=True)
            nums = out.split('\n')
            for num in nums:
                i += 1
                if i == 1:
                    killid = num
            os.system("sudo kill " + killid)
        if LEDS == 1:
            GPIO.output(GOODVOLTPIN, GPIO.LOW)
            GPIO.output(LOWVOLTPIN, GPIO.HIGH)
	os.system("/usr/bin/omxplayer --no-osd --layer 999999 lowbattshutdown.mp4 --alpha 160;sudo shutdown -h now")
        status = 0
    elif ret < 800:
        # 25-0%
        # Low battery warning: Switch LED to red, play warning clip
        if status != 25:
            if LEDS == 1:
                GPIO.output(GOODVOLTPIN, GPIO.LOW)
                GPIO.output(LOWVOLTPIN, GPIO.HIGH)
            os.system(PNGVIEWPATH + "/pngview -b 0 -l 300003 -x 650 -y 5 " + ICONPATH + "/battery25.png &")
            if DEBUGMSG == 1:
                print("Changed battery icon to 25")
            out = check_output("ps aux | grep pngview | awk '{ print $2 }'", shell=True)
            nums = out.split('\n')
            for num in nums:
                i += 1
                if i == 1:
                    killid = num
            os.system("sudo kill " + killid)
        if warning == 0:
            warning = 1
            os.system("/usr/bin/omxplayer --no-osd --layer 999999 lowbattalert.mp4 --alpha 160 ");
        status = 25
    elif ret < 830:
        # 50-25%
        if status != 50:
            if LEDS == 1:
                GPIO.output(GOODVOLTPIN, GPIO.HIGH)
                GPIO.output(LOWVOLTPIN, GPIO.LOW)
            os.system(PNGVIEWPATH + "/pngview -b 0 -l 300002 -x 650 -y 5 " + ICONPATH + "/battery50.png &")
            if DEBUGMSG == 1:
                print("Changed battery icon to 50")
            out = check_output("ps aux | grep pngview | awk '{ print $2 }'", shell=True)
            nums = out.split('\n')
            for num in nums:
                i += 1
                if i == 1:
                    killid = num
            os.system("sudo kill " + killid)
        status = 50
    elif ret < 860:
        # 75-50%
        if status != 75:
            if LEDS == 1:
                GPIO.output(GOODVOLTPIN, GPIO.HIGH)
                GPIO.output(LOWVOLTPIN, GPIO.LOW)
            os.system(PNGVIEWPATH + "/pngview -b 0 -l 300001 -x 650 -y 5 " + ICONPATH + "/battery75.png &")
            if DEBUGMSG == 1:
                print("Changed battery icon to 75")
            out = check_output("ps aux | grep pngview | awk '{ print $2 }'", shell=True)
            nums = out.split('\n')
            for num in nums:
                i += 1
                if i == 1:
                    killid = num
            os.system("sudo kill " + killid)
        status = 75
    else:
        # 100-75%
        if status != 100:
            if LEDS == 1:
                GPIO.output(GOODVOLTPIN, GPIO.HIGH)
                GPIO.output(LOWVOLTPIN, GPIO.LOW)
            os.system(PNGVIEWPATH + "/pngview -b 0 -l 300000 -x 650 -y 5 " + ICONPATH + "/battery100.png &")
            if DEBUGMSG == 1:
                print("Changed battery icon to 100")
            out = check_output("ps aux | grep pngview | awk '{ print $2 }'", shell=True)
            nums = out.split('\n')
            for num in nums:
                i += 1
                if i == 1:
                    killid = num
            os.system("sudo kill " + killid)        
        status = 100

    # Pause before starting loop once again
    time.sleep(REFRESH_RATE / 1000)
