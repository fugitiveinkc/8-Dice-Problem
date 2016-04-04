import random

class dice:
	def __init__(self, elements):
		self.faces = elements
		self.face = None
	
	def roll(self):
		self.face = self.faces[random.randrange(0,len(self.faces),1)]
