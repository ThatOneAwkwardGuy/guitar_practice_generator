class Exercise:
	'''base class definition for exercises'''
	def __init__(self, e_type, level, text, time):

		self.type = e_type
		self.level = level
		self.text = text
		self.time = time
