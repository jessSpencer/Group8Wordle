# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
import enchant
import time

# this is bringing in the dictionary
d = enchant.Dict("en_US")


def wordle():

  def enter_action(s):
    # End the game if they have filled out all the rows
    if (gw.get_current_row() > 5):
      quit()
    
    # compiles the guess from the letters in each square
    guess = ""
    j = 0
    while j < N_COLS:
      guess += gw.get_square_letter(gw.get_current_row(), j).lower()
      j += 1

    # Have to remove spaces from the word
    guess = guess.strip()
    tempWord = randomWord
    # Checks to make sure they entered a five letter english word
    if len(guess) == 5:
      if (d.check(guess)) == True:
        # Iterates through each letter in the guess. Sets the square and keyboard to the appropriate color.
        for index, char in enumerate(guess):
          # Sets the keyboard color to green if in the word and in the right place
          if char == tempWord[index]:
            gw.set_square_color(gw.get_current_row(), index,"#66BB66")
            gw.set_key_color(char.upper(), "#66BB66")
            tempWord = tempWord.replace(char,"*", 1)
        for index, char in enumerate(guess):
          # Sets the keyboard color to yellow if in the word, but not in the right place
          if char in tempWord:
            gw.set_square_color(gw.get_current_row(), index,"#CCBB66" )
            gw.set_key_color(char.upper(), "#CCBB66")
            tempWord = tempWord.replace(char,"*", 1)
          # Sets rest of letters to grey
          elif gw.get_square_color(gw.get_current_row(), index) not in ["CCBB66","#66BB66"]:
            gw.set_square_color(gw.get_current_row(), index,"#999999")
            gw.set_key_color(char.upper(), "#999999")
        # If they are on the last row,and the guess does not equal the random word, they lost!
        if (gw.get_current_row()==5 and guess != randomWord):
          print("Entered Break Condition")
          gw.show_message(f"Sorry, the word was '{randomWord}'.")
        # If the guess is equal to the random word, they won!
        elif (guess == randomWord):
          gw.show_message(f"Congratulations! You guessed the word in {gw.get_current_row() + 1} tries!")
          # No more guesses
          gw.set_current_row(6)
        gw.set_current_row(gw.get_current_row()+1)
      else:
        gw.show_message("Not a Word 😕")
    else:
      gw.show_message("Please enter a 5 letter word") 

    
  
  gw = WordleGWindow()
  randomWord = random.choice(FIVE_LETTER_WORDS)
  gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
  wordle()


