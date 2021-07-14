## Libraries
from gpiozero import Button
import multiprocessing
from signal import pause

from globalvariables import RASPBERRY_PINS, FAN_CONFIG, BUTTON_TRIGGERED, DISPLAY_MODE

class ButtonController(multiprocessing.Process):
	def __init__(self, name, function, var_name):
		multiprocessing.Process.__init__(self)
		self.pin = RASPBERRY_PINS[name]
		self.function = function
		self.variable = var_name

	def setup(self):
		'''
		Sets up the button
		'''
		self.button = Button(self.pin)
		self.button.when_pressed = self.function
		pause()
	
	def run(self):
		'''
		Runs the process
		'''
		self.setup()

def modifyFanState():
	'''
	Modifies the state for the Fan
	First, turning it on
	Second, increase potency
	Third, turning it off
	'''
	print('Modify fan state called.')
	if not FAN_CONFIG['state']:
		FAN_CONFIG['state'] = True
	elif not fan['potency']:
		FAN_CONFIG['potency'] = True
	else:
		FAN_CONFIG['state'] = False
		FAN_CONFIG['potency'] = False
	BUTTON_TRIGGERED = True

def modifyDisplayMode():
	'''
	Modifies the state for the display
	False, Temperature
	True, Humidity
	'''
	print('Modify mode called.')
	DISPLAY_MODE = not DISPLAY_MODE
	BUTTON_TRIGGERED = True
