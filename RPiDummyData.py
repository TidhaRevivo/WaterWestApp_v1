import RPi.GPIO as GPIO
import time
import math
from pyrebase import pyrebase
import json


# Get RPi's CPU ID _______________________________________
def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"
 
  return cpuserial

# __________________________________________


# Connetcting to DB _____________________________________________-
config = {
  "apiKey": "GrlM80waITypgrHp2K2mWCO0Td6zDI2TFBprdh8h",
  "authDomain": "dummy-project-4b51c.firebaseapp.com",
  "databaseURL": "https://dummy-project-4b51c-default-rtdb.firebaseio.com/",
  "storageBucket": "dummy-project-4b51c.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
# _______________________________________________________________

CpuSerial= getserial() #CPU Serial number- basically RPi ID
GPIO.setmode(GPIO.BOARD) #Set mode to work with pin numbers and not ...
GPIO.setup(18,GPIO.OUT) #trigger
GPIO.setup(16,GPIO.IN) #echo
Radius = 0.129 #meters
Height = 0.38 #meters
Full_Tank = 20 #leters

# my_time = time.strftime('%Y-%m-%d', time.localtime(time.time())) #code to trasnfer time.time() to Date

# Full_Tank = math.pi * Radius ** 2 * Height * 1000


# DELAY = 0.0000275763773705539


while True:
	try:
		GPIO.output(18, False)
		time.sleep(2) #Give sensor time to settle

		#trigger the sonar
		GPIO.output(18, True) 
		time.sleep(0.00001)
		GPIO.output(18, False)

		#read the echo
		while GPIO.input(16)==0:
			pulse_start = time.time()
		while GPIO.input(16)==1:
			pulse_end = time.time()

		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration * 171.5
		distance = round(distance, 2) #round it to two decimal place
		Empty_Tank = math.pi * Radius ** 2 * distance * 1000
		Water = round((Full_Tank - Empty_Tank), 3)
		data = {
			str(time.strftime('%Y-%m-%d', time.localtime(time.time()))): Water
		}
		
		# print (str(Full_Tank) + " - " + str(Empty_Tank) + " = " + str(Water))
		print(str(distance * 100) + "cm", str(time.time()).split('.')[0])
		db.child("RaspberryPis").child(CpuSerial).child(str(time.time()).split('.')[0]).push(data)
	#cleanup on ctr c
	except KeyboardInterrupt:
		GPIO.cleanup()



