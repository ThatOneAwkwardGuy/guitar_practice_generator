import random

def random_scale_generator(number_of_notes):
	'''
	generates a scale based on the
	user-declared number of notes
	always includes the root note

	(int) -> set

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

def print_test_scales():
	for n in range(1, 12):
		print(n, random_scale_generator(n))

print_test_scales()
