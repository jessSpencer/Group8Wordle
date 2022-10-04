# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
import enchant

# this is bringing in the dictionary
d = enchant.Dict("en_US")


def wordle():

    def enter_action(s):
        # this is checking to make sure they entered in a 5 letter word
        if len(str(gw.get_current_row())) == 5:
            # this is checking to make sure the word entered is valid
            if (d.check(gw.get_current_row())) == True:
                print("Nice guess!")
            # this is the response they get if they enter in a word that is not valie
            else:
                print("I'm sorry, please enter in an actual word")
            # if the word is less or more than 5 letters they get this response
        else:
            print("Please enter a 5 letter word")

        j = 0
        while j < N_COLS:
            if gw.get_square_letter(gw.get_current_row(), j).lower() not in randomWord:
                gw.set_square_color(gw.get_current_row(), j,"#999999")
                # Sets the keyboard color grey if not in the word
                gw.set_key_color(gw.get_square_letter(gw.get_current_row(), j), "#999999")
            elif gw.get_square_letter(gw.get_current_row(), j).lower() == randomWord[j]:
                gw.set_square_color(gw.get_current_row(), j,"#66BB66")
                # Sets the keyboard color to green if in the word and in the right place
                gw.set_key_color(gw.get_square_letter(gw.get_current_row(), j), "#66BB66")
            else:
                gw.set_square_color(gw.get_current_row(), j,"#CCBB66" )
                # Sets the keyboard color to yellow if in the word, but not in the right place
                gw.set_key_color(gw.get_square_letter(gw.get_current_row(), j), "#CCBB66")
                
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


