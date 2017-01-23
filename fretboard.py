import copy

from generator import *
from scale import *

STANDARD_TUNING = ['e', 'b', 'g', 'd', 'a', 'e']

class Fretboard:

	def __init__(self, tuning=STANDARD_TUNING):
		self.tuning = map(lambda x: x.lower(), tuning)
		self.strings = [string_generator(note.lower()) for note in self.tuning]

	# def generate_strings(self):
	# 	'''returns list of lists
	# 	generates strings of fretboard'''
	# 	ret = []
	# 	for note in tuning:
	# 		ret.append(string_generator(note.lower()))
	# 	return ret

	def show_scale(self, scale):
		# TODO: amend this docstring
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
		strings_copy = copy.deepcopy(self.strings)
		sample_string = string_generator(scale.root)
		scale_notes = [sample_string[note] for note in scale.recipe]
		for idx, string in enumerate(strings_copy):
			for note in string:
				if note == scale.root:
					string[string.index(note)] = 'R'
				elif note in scale_notes:
					string[string.index(note)] = 'O'
				else:
					string[string.index(note)] = '-'
			strings_copy[idx] = ' | '. join(string)
		return strings_copy
