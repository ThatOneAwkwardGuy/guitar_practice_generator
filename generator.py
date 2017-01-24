# WELCOME CONTRIBUTORS, THIS IS A VERY EARLY STAGE, PLEASE EXCUSE THE INITIAL MESS ;)

import random

STANDARD_TUNING = ['E', 'B', 'G', 'D', 'A', 'E']

# not in use really at the moment.
def fretboard_printer(tuning):
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

def fretboard_generator(tuning=STANDARD_TUNING):
	'''(list) - > list of lists
	generates a fretboard'''
	fretboard = []
	for note in tuning:
		fretboard.append(string_generator(note.lower()))
	return fretboard

def permutation_generator(n=4, allow_repeats=True):
	'''generates a alternate picking exercise
	based on one of permutations of 1...n.
	n is restricted to <= 9
	'''
	n = 4 if n > 4 else n
	# options is just a list of integers 1 to n, converted to strings
	options = list(map(lambda x: str(x), range(1, n + 1)))
	if allow_repeats:
		result = ''.join([random.choice(options) for _ in range(n)])
	else:
		random.shuffle(options)
		result = ''.join(options)
	return result

def print_part_fretboard(range, fretboard):
	'''prints a part of the fretboard between given frets'''
	pass

if __name__ == '__main__':
	pass
