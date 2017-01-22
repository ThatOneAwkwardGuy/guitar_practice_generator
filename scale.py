import random

scales ={
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

	def __init__(self, number, root):
		'''scale class'''
		self.root = root.lower()
		self.recipe = self.random_scale_generator(number)
		self.tuning = ['E', 'B', 'G', 'D', 'A', 'E']
		self.fretboard = self.fretboard_generator(self.tuning)
		self.scale_pattern = self.scale_string_translator(root, self.recipe, self.fretboard)

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

	def string_generator(self, note):
		'''(string) -> list
		builds a map of the notes on a string of a given tuning'''
		# need to build in a string input validator for bb, db, eb etc
		# use re
		base_string = ['e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b', 'c', 'c#', 'd', 'd#']
		index = base_string.index(note)
		string = (base_string[index:] + base_string[:index]) * 2
		string.append(note)
		return string

	def fretboard_generator(self, tuning):
		'''(list) - > list of lists
		generates a fretboard'''
		fretboard = []
		for note in tuning:
			fretboard.append(self.string_generator(note.lower()))
		return fretboard

	def scale_string_translator(self, root, scale, fretboard):
		'''(list, string, list) -> list
		translates the scale formula into symbols depicting root note
		and other notes

		the function should take in the scale, a list of integers and the root note,
		and translate the list into a list of symbols where X is the root note,
		 O is any other scale note, and the rest are changed into hyphens.

		>>> scale_string_translator(major_scale, C)
		['O', 'O', '-', 'O', '-', 'O', '-', 'O', 'X', '-', 'O', '-']  # this is on the E string

		root is R
		every index in scale stays rest is replaced by '-'
		everythin that's not R or - is replaced by O

		create a string that's a root string, cut it in half
		map out which notes are IN SCALE, and this list will be used
		to replace the notes with '-' 's and 'o' 's
		'''
		sample_string = self.string_generator(root)[:12]
		scale_notes = []
		for note in scale:
			scale_notes.append(sample_string[note])
		for string in fretboard:
			for note in string:
				if note == root:
					string[string.index(note)] = 'R'
				elif note in scale_notes:
					string[string.index(note)] = 'O'
				else:
					string[string.index(note)] = '-'

		return fretboard

	def print_part_fretboard(range, fretboard):
		'''prints a part of the fretboard between given frets'''
		pass

