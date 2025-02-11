import random as rdm
import string

#Player 2 gives Player 1 a word to guess.
Word = list(input('Input a valid word to begin the game: ').upper())
#Adds Alphabet list to crossreference Given word.
Alphabet = list(string.ascii_uppercase)
#Check that the word is valid.
Valid = all(e in Alphabet for e in Word)
#if word given was invalid loops until a valid word is given
while Valid != True:
    Word = list(input('Input a valid word to begin the game: ').upper())
    Alphabet = list(string.ascii_uppercase)
    Valid = all(e in Alphabet for e in Word)

