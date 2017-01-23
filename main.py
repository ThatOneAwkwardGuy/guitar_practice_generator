# WELCOME CONTRIBUTORS, THIS IS A VERY EARLY STAGE, PLEASE EXCUSE THE INITIAL MESS ;)

import exercise
from generator import *
from scale import *
from fretboard import *

def routine_printer( scale_gen):
	'''test'''
	print('Practice routine')
	print('Random scale:', scale_gen)
	print('Alternate picking pattern:', permutation_generator())


#mockup of the output
print('scale to practice: e minor')
f_board = Fretboard()
e_minor_scale = Scale('e', DEFAULT_SCALES['minor'])
for string in f_board.show_scale(e_minor_scale):
	print (string)
print('\n')

print('arpeggio to practice: c major')
c_maj_arp = Scale('c', [0, 4, 7])
for string in f_board.show_scale(c_maj_arp):
	print (string)
print('\n')

print('picking /left hand exercise: ')
print(permutation_generator())
