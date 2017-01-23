# WELCOME CONTRIBUTORS, THIS IS A VERY EARLY STAGE, PLEASE EXCUSE THE INITIAL MESS ;)

import arpeggio, exercise
from generator import *
from scale import *
from fretboard import *

arpeggio = arpeggio.Arpeggio('major', [0, 4, 7])

def routine_printer(arpeggio, scale_gen):
	'''test'''
	print('Practice routine')
	print('Arpeggio:', arpeggio.name, arpeggio.recipe)
	print('Random scale:', scale_gen)
	print('Alternate picking pattern:', permutation_generator())


#mockup of the output
print('scale to practice: e minor')
f_board = Fretboard()
e_minor_scale = Scale('e', [0,2,3,5,7,8,10])
for string in f_board.show_scale(e_minor_scale):
	print string
print('\n')

print('arpeggio to practice: c major')
c_maj_arp = Scale('c', [0, 4, 7])
for string in f_board.show_scale(c_maj_arp):
	print string
print('\n')

print('picking /left hand exercise: ')
print(permutation_generator())
