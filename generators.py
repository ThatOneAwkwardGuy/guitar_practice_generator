import random

def random_scale_generator(number_of_notes):
	'''
	generates a scale based on the
	user-declared number of notes
	always includes the root note

	(int) -> set

	IMPORTANT: Doctests will fail.

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

fretrboard_printer(tuning)
