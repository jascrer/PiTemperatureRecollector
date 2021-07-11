## Libraries
import sys
import time
import adafruit_dht

from globalvariables import RASPBERRY_PINS

class DHTController:
	def __init__(self):
		self.sensor = adafruit_dht.DHT11(RASPBERRY_PINS["DHT_PIN"])

	def getTemperature(self):
		'''
		Returns the temperature from the sensor
		'''
		return self.sensor.temperature

	def getHumidity(self):
		'''
		Returns the humidity from the sensor
		'''
		return self.sensor.humidity

# Example of how to use the class to get temperatures
#controller = DHTController()
#temp = controller.getTemperature()
#humi = controller.getHumidity()
#counter = 0
#while counter < 10:
#	print('Temperatura={0:0.1f} C  Humedad={1:0.1f}%'.format(temp, humi))#
#	time.sleep(1)
#	counter += 1
