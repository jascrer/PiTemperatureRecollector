## Libraries
import RPi.GPIO as GPIO
import time

from globalvariables import RASPBERRY_PINS, CHARACTERS

class DisplayController:
	def __init__(self):
		self.digit_characters = [' ', ' ', 'Degree', 'A']
		self.mode = False
		self.turnFan(False)

	def resetDisplay(self):
		if GPIO.getmode() != 11:
			GPIO.setmode(GPIO.BCM)

		self.segments = (RASPBERRY_PINS["A"], RASPBERRY_PINS["B"],
			RASPBERRY_PINS['C'], RASPBERRY_PINS['D'],
			RASPBERRY_PINS['E'], RASPBERRY_PINS['F'],
			RASPBERRY_PINS['G'], RASPBERRY_PINS['DP'])
		self.digits = (RASPBERRY_PINS['D1'], RASPBERRY_PINS['D2'],
			RASPBERRY_PINS['D3'], RASPBERRY_PINS['D4'])

		for segment in self.segments:
			GPIO.setup(segment, GPIO.OUT)
			GPIO.output(segment, 1)

		for digit in self.digits:
			GPIO.setup(digit, GPIO.OUT)
			GPIO.output(digit, 0)

	def setCharacter(self, character, digit):
		'''
		Sets the character for each digit
		'''
		if digit == 'D1':
			self.digit_characters[0] = character
		elif digit == 'D2':
			self.digit_characters[1] = character
		elif digit == 'D3':
			self.digit_characters[2] = character
		elif digit == 'D4':
			self.digit_characters[3] = character

	def setMode(self):
		'''
		Sets the mode for the information that it is being shown
		False: Temperature
		True: Humidity
		'''
		if self.mode:
			self.setCharacter('H','D3')
		else:
			self.setCharacter('Degree', 'D3')
		self.mode = not self.mode

	def turnFan(self, on):
		'''
		Sets if the fan is on or off
		on: True, L = low potency
		off: False: A = turned off
		'''
		if on:
			self.setCharacter('L','D4')
		else:
			self.setCharacter('A','D4')

	def increasePotency(self, increase, on):
		'''
		Sets if the potency was increased or decreased
		Increase: True, H: high potency
		Decrease: False, turnFan function is called
		'''
		if increase:
			self.setCharacter('H', 'D4')
		else:
			self.turnFan(on)

	def setValue(self, value):
		'''
		Sets the value to be displayed
		'''
		strValue = str(value)
		self.setCharacter(strValue[0], 'D1')
		self.setCharacter(strValue[1], 'D2')

	def display(self):
		'''
		Displays each character
		'''
#		try:
#			while True:
		self.resetDisplay()
		for digit in range(4):
			GPIO.output(self.digits[digit], 0)
			for segment in range(8):
				character = self.digit_characters[digit]
				GPIO.output(self.segments[segment], CHARACTERS[character][segment])
			GPIO.output(self.digits[digit], 1)
			time.sleep(0.001)
			GPIO.output(self.digits[digit], 0)
#		except:
#			print('Error on the display')

	def onDestroy(self):
		'''
		Cleans up the pins
		'''
		GPIO.cleanup()

#display = DisplayController()
#display.setCharacter('2','D1')
#display.setCharacter('3','D2')
#display.setCharacter('Degree','D3')
#display.setCharacter('A','D4')
#display.display()
#time.sleep(10)
#display.onDestroy()
