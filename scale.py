#encoding=utf-8
import random
from generator import *

DEFAULT_SCALES = {
	'chromatic' : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
	'major': [0, 2, 4, 5, 7, 9, 11],
	'minor': [0, 2, 3, 5, 7, 8, 10],
	'blues': [0, 3, 5, 6, 7, 10]
}

# every integer represents the distance from the root note
# 0 is the root note, 7 is a perfect 5th, 3 is a minor 3rd etc
# the possible intervals are from the root up until major 7th
# using lists for scales and arpeggios

class Scale:

	def __init__(self, root, recipe=None):
		'''scale class'''
		self.root = root.lower()
		# case of no recipe seems unneccessary
		if not recipe:
			self.recipe = self.random_scale_generator(5)
		else:
			self.recipe = recipe
		# self.tuning = ['E', 'B', 'G', 'D', 'A', 'E']
		# self.fretboard = fretboard_generator(self.tuning)

	def random_scale_generator(self, number_of_notes):
		'''
		generates a scale based on the
		user-declared number of notes
		always includes the root note
		(int) -> set
		'''
		scale = set()
		scale.add(0)
		while len(scale) != number_of_notes:
			scale.add(random.randint(1, 11))
		return scale

	def print_part_fretboard(range, fretboard):
		'''prints a part of the fretboard between given frets'''
		pass
