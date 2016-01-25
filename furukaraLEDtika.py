# robosys
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

a = 1
COUNT = 100
PIN1 = 25
PIN2 = 24
PIN3 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN1,GPIO.OUT)
GPIO.setup(PIN2,GPIO.OUT)
GPIO.setup(PIN3,GPIO.OUT)
green = GPIO.PWM(PIN3, 50)
red = GPIO.PWM(PIN2, 50)
blue = GPIO.PWM(PIN1, 50)

red.start(0)
blue.start(0)
green.start(100)

T = 0.04
I = 0
time.sleep(0.5)

for _ in xrange(0, COUNT):
	blue.ChangeDutyCycle(I)
	green.ChangeDutyCycle(100-I)
	time.sleep(T)
	I+=1

I = 0

for _ in xrange(0, COUNT):
	red.ChangeDutyCycle(I)
	blue.ChangeDutyCycle(100-I)
	I+=1
	time.sleep(T)
I = 0

for _ in xrange(0, COUNT):
	red.ChangeDutyCycle(100-I)
	green.ChangeDutyCycle(I)
	I+=1
time.sleep(T)

time.sleep(0.5)

red.stop()
green.stop()
blue.stop()
	
	
GPIO.cleanup()
