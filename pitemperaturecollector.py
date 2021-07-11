from dhtcontroller import DHTController
from displaycontroller import DisplayController
import RPi.GPIO as GPIO
import time


def main():	
	dht_controller = DHTController()
	display_controller = DisplayController()
	while True:
		try:
			temperatura = dht_controller.getTemperature()
			#print(f'temperature={temperatura}')
			#time.sleep(1)
			display_controller.setValue(temperatura)
			display_controller.display()
		finally:
			GPIO.cleanup()

main()
