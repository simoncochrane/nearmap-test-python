import time

class DBStore:
	def __init__(self):
		self.values = {}

	def get_value(self, name):
		# simulate 50 ms roundtrip to database
		time.sleep(0.05)

		return self.values[name]

	def set_value(self, name, value):
		# simulate 50 ms roundtrip to database
		time.sleep(0.05)

		self.values[name] = value
