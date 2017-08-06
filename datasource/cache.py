import time

class CacheStore:
	def __init__(self):
		self.values = {}

	def get_value(self, name):
		# simulate 5 ms roundtrip to distributed cache
		time.sleep(0.005)

		return self.values[name]

	def set_value(self, name, value):
		# simulate 5 ms roundtrip to distributed cache
		time.sleep(0.005)

		self.values[name] = value
