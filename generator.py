# WELCOME CONTRIBUTORS, THIS IS A VERY EARLY STAGE, PLEASE EXCUSE THE INITIAL MESS ;)

import random

def random_scale_generator(number_of_notes):
	'''
	generates a scale based on the
	user-declared number of notes
	always includes the root note

	(int) -> set

	IMPORTANT: Doctests will fail, the scales are random every time.
	## Does anyone know what might be causing this?

	>>> random_scale_generator(3)
	{0, 3, 6}
	>>> random_scale_generator(7)
	{0, 2, 3, 5, 6, 10, 11}
	>>> random_scale_generator(4)
	{0, 3, 7, 11}
	'''
	scale = set()
	scale.add(0)
	while len(scale) != number_of_notes:
		scale.add(random.randint(1, 11))
	return scale

def fretrboard_printer(tuning):
	''' really ok prints the fretboard, but does not really
	well handle the modularity - in this implementation,
	the fretboard is only a printable set of strings, and
	I would like it to be an object that I will be able to
	show the scales on.'''
	string = '|-|'+''.join(['-' for n in range(24)])
	for letter in tuning:
		print(letter + string + '|')
	print(' ' * 6 + 'X' + ((' ' + 'X') * 2) + ' ' * 2 + 'X' + ' ' + 'X' +
		  ' ' * 2 + 'X' + ((' ' + 'X') * 2) + ' ' * 2 + 'X' + ' ' + 'X')

tuning = ['E', 'B', 'G', 'D', 'A', 'E']

def string_generator(note):
	'''(string) -> list
	builds a map of the notes on a string of a given tuning'''
	# need to build in a string input validator for bb, db, eb etc
	# use re
	base_string = ['e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b', 'c', 'c#', 'd', 'd#']
	index = base_string.index(note)
	string = (base_string[index:] + base_string[:index]) * 2
	string.append(note)
	return string

def fretboard_generator(tuning):
	'''(list) - > list of lists
	generates a fretboard'''
	fretboard = []
	for note in tuning:
		fretboard.append(string_generator(note))
	return fretboard

def scale_string_translator(root, scale, fretboard):
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
	sample_string = string_generator(root)[:12]
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



def permutations_generator():
	'''generates a alternate picking exercise
	based on one of 24 permutations of the
	1234 combination
	'''
	options = [1, 2, 3, 4]
	result = ''
	while len(result) != 4:
		number = random.choice(options)
		result += str(number)
	return result

def print_part_fretboard(range, fretboard):
	'''prints a part of the fretboard between given frets'''
	pass

if __name__ == '__main__':
	pass
