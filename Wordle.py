# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
import enchant
# this is bringing in the dictionary
d = enchant.Dict("en_US")
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
	def enter_action(s):
		j = 0
		while j < N_COLS:
			if gw.get_square_letter(gw.get_current_row(), j).lower() not in randomWord:
				gw.set_square_color(gw.get_current_row(), j,"#999999")
			elif gw.get_square_letter(gw.get_current_row(), j).lower() == randomWord[j]:
				gw.set_square_color(gw.get_current_row(), j,"#66BB66")
			else:
				gw.set_square_color(gw.get_current_row(), j,"#CCBB66" )
			j+=1
		gw.set_current_row(gw.get_current_row()+1)
		if (gw.get_current_row()==6):
			quit()		
	
	gw = WordleGWindow()
	randomWord = random.choice(FIVE_LETTER_WORDS)
	for index, char in enumerate(randomWord):
		gw.set_square_letter(0, index, char)
	
	gw.add_enter_listener(enter_action)
	gw.set_current_row(gw.get_current_row()+1)

# Startup code

if __name__ == "__main__":
	wordle()
