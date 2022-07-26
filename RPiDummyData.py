import time
import math
import random
import sys
import RPi.GPIO as GPIO
from pyrebase import pyrebase

# config = {
# 	"apiKey": "GrlM80waITypgrHp2K2mWCO0Td6zDI2TFBprdh8h",
# 	"authDomain": "dummy-project-4b51c.firebaseapp.com",
# 	"databaseURL": "https://dummy-project-4b51c-default-rtdb.firebaseio.com/",
# 	"storageBucket": "dummy-project-4b51c.appspot.com"
# }

# firebase = pyrebase.initialize_app(config)
# db = firebase.database()
GPIO.setmode(GPIO.BOARD)
TRIG = 16  # 23 BCM
ECHO = 18  # 24 BCM


def callback(test_input):
	print('signal received!', test_input)
	return True


# SetUp
GPIO.setup(TRIG,GPIO.OUT, initial=0)
GPIO.setup(ECHO,GPIO.IN)
GPIO.add_event_detect(ECHO, GPIO.RISING, callback=callback)
time.sleep(1)
print('waiting for signal')

	
	
	
while True:
# it would be a good idea to start timing here -- suggestion from Julian
	GPIO.output(TRIG, 1)
	start= time.time()
	
	time.sleep(0.00001)
	GPIO.output(TRIG, 0)
	time.sleep(2)
		
#  caculations
	# # while GPIO.input(ECHO)==0:
	# 	pulse_start = time.time()
	# while GPIO.input(ECHO)==1:
	# 	 pulse_end = time.time()
	# pulse_duration = pulse_end - pulse_start
	# D = pulse_duration * 17150
	# D = round(D, 2)
	# E = math.pi * 10 * 2 * D * 1000
	# MW = math.pi * 10 * 2 * 200 *1000
	# W = MW - E
	# print(W)
