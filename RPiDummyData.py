import RPi.GPIO as GPIO
import time
import math
from pyrebase import pyrebase

config = {
  "apiKey": "GrlM80waITypgrHp2K2mWCO0Td6zDI2TFBprdh8h",
  "authDomain": "dummy-project-4b51c.firebaseapp.com",
  "databaseURL": "https://dummy-project-4b51c-default-rtdb.firebaseio.com/",
  "storageBucket": "dummy-project-4b51c.appspot.com"
}

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

firebase = pyrebase.initialize_app(config)
db = firebase.database()
CpuSerial= getserial()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT) #trigger
GPIO.setup(16,GPIO.IN) #echo
Radius = 0.129 #meters
Height = 0.38 #meters
Full_Tank = 20
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

		#calculate distance in centemeteres
		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration * 171.5
		distance = round(distance, 2) #round it to two decimal place
		Empty_Tank = math.pi * Radius ** 2 * distance * 1000
		Water = Full_Tank - Empty_Tank
		data = {
			"Water Level" : Water,
			"Date" : Time.time()
		}
		
		print (str(Full_Tank) + " - " + str(Empty_Tank) + " = " + str(Water))
		print(distance, CpuSerial)
		db.child("Water_Level_Db").child(CpuSerial).push(data)
	#cleanup on ctr c
	except KeyboardInterrupt:
		GPIO.cleanup()



