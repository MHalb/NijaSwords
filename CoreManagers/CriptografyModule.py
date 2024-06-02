import hashlib

class CriptografyManager:
	def __init__(self):
		with open("tempdb.json", 'r') as r:
			self.tempdb = json.load(r)
