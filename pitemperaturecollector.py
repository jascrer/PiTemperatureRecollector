from dhtcontroller import DHTController
from displaycontroller import DisplayController
from buttoncontroller import *

import RPi.GPIO as GPIO
import time

from globalvariables import FAN_CONFIG, BUTTON_TRIGGERED, DISPLAY_MODE

class PiTemperatureCollector:
	def __init__(self):
		self.dht_controller = DHTController()
		self.display_controller = DisplayController()
		self.button_mode = ButtonController('BUTTON_1', modifyDisplayMode, 'DISPLAY_MODE')
		self.button_fan = ButtonController('BUTTON_2' , modifyFanState, 'FAN_CONFIG')
		
	def displayReboot(self, value):
		'''
		Updates the display
		'''
		if self.display_controller.is_alive():
			self.display_controller.terminate()
			self.display_controller = DisplayController()
		self.display_controller.setMode(DISPLAY_MODE)
		self.display_controller.setValue(value)
		self.display_controller.increasePotency(FAN_CONFIG['potency'],FAN_CONFIG['state'])
		self.display_controller.start()

	def getValueFromSensor(self):
		'''
		Gets the value from the sensor depending on the mode
		mode = False, Temperature
		mode = True, Humidity
		'''
		if DISPLAY_MODE:
			return self.dht_controller.getHumidity()
		else:
			return self.dht_controller.getTemperature()

	def execute(self):
		'''
		Initiates the collector
		'''
		no_error = True
		while no_error:
			try:
				if GPIO.getmode() != 11:
					GPIO.setmode(GPIO.BCM)
				value = self.getValueFromSensor()
				print(f'Actual temperature = {value}')
				self.displayReboot(value)
				time.sleep(5)
			except Exception as e:
				print(f'Exception: {e}')
				if self.display_controller.is_alive():
					self.display_controller.terminate()
					self.display_controller.join()
				no_error = False
			finally:
				GPIO.cleanup()
		self.display_controller.terminate()
		self.display_controller.join()
		

if __name__ == '__main__':
	#buttonMode = Button(18)
	#buttonFan = Button(23)
	#buttonMode.when_pressed = modifyMode
	#buttonFan.when_pressed = modifyFanState
	try:
		collector = PiTemperatureCollector()
		collector.execute()
	except KeyboardInterrupt:
		GPIO.cleanup()
