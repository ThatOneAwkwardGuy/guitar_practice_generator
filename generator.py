# WELCOME CONTRIBUTORS, THIS IS A VERY EARLY STAGE, PLEASE EXCUSE THE INITIAL MESS ;)

import random


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

tuning = ['E', 'B', 'G', 'D', 'A', 'E']

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
