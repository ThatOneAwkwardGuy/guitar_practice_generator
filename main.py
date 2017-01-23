# WELCOME CONTRIBUTORS, THIS IS A VERY EARLY STAGE, PLEASE EXCUSE THE INITIAL MESS ;)

import arpeggio, exercise, generator, scale

arpeggio = arpeggio.Arpeggio('major', [0, 4, 7])

def routine_printer(arpeggio, scale_gen):
	'''test'''
	print('Practice routine')
	print('Arpeggio:', arpeggio.name, arpeggio.recipe)
	print('Random scale:', scale_gen)
	print('Alternate picking pattern:', generator.permutations_generator())


#mockup of the output
print('scale to practice: e minor')
f_board = generator.fretboard_generator(['e', 'b', 'g', 'd', 'a', 'e'])
for string in generator.scale_string_translator('e', [0,2,3,5,7,8,10], f_board):
	print (''.join(string))
print()

print('arpeggio to practice: c major')

f_board = generator.fretboard_generator(['e', 'b', 'g', 'd', 'a', 'e'])
for string in generator.scale_string_translator('c', [0, 4, 7], f_board):
	print (''.join(string))
print()

print('picking /left hand exercise: ')
print(generator.permutations_generator())
