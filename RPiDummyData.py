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

START_TIME = None
END_TIME = None
DELAY = 0.0011711221822102865

def callback(test_input):
	END_TIME = time.time()
	time_delta = END_TIME - START_TIME + DELAY
	distance = time_delta * 343 / 2
	Empty_Tank = math.pi * 0.135 * 2 * distance * 1000
	Full_Tank = math.pi * 0.135 * 2 * 0.44 * 1000
	Water = Full_Tank - Empty_Tank
	print(time_delta)



# SetUp
GPIO.setup(TRIG,GPIO.OUT, initial = 0)
GPIO.setup(ECHO,GPIO.IN)
GPIO.add_event_detect(ECHO, GPIO.RISING, callback = callback)
time.sleep(1)
print('waiting for signal')


while True:
	GPIO.output(TRIG, 1)
	START_TIME = time.time()
	time.sleep(0.00001)
	GPIO.output(TRIG, 0)
	time.sleep(1)

		

