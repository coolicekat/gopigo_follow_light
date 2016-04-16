#! /usr/bin/env python

#from gopigo import *
import time
import gopigo

#gopigo.fwd()
#time.sleep(2)
#gopigo.bwd()
#time.sleep(2)
gopigo.stop()

sensor_pin = gopigo.analogPort
gopigo.pinMode(sensor_pin,"INPUT")

# calibrate light sensor
print("Calibrating Light Sensor")
base_value = 0
sample_size = 50
light_threshold = 30
for i in range (1, sample_size):
	base_value = base_value + gopigo.analogRead(sensor_pin)

base_light_value = base_value/sample_size

print(base_light_value)
print("Finished calibration")

while True:
	try:
		current_light_value = gopigo.analogRead(sensor_pin)
		print (current_light_value)
		time.sleep(.5)
		if current_light_value > base_light_value + light_threshold:
			print("GOpiGO")
			gopigo.fwd()
			time.sleep(1)
		else:
			gopigo.stop()

	except IOError:
		print  ("Error")


