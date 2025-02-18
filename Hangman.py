import random as rdm
import string
import getpass

def valid_word():
    valid = False
    while valid == False:
        word =(getpass.getpass("Input a valid word to begin the game: ").upper())
        word_letters = set(word)
        alphabet = set(string.ascii_uppercase)
        valid = all(e in alphabet for e in word_letters)
    return (word)

def hangman():
    word = valid_word()
    word_letters = set(word)
    alphabet_letters = set(string.ascii_uppercase)
    used_letters = set()
    lives = 10

    while len(word_letters) > 0 and lives > 0:
        print(f"Lives Left: {lives}")
        print("you have used these letters: ", " ".join(used_letters))
        hidden_word = [letter if letter in used_letters else "_" for letter in word]
        print("Current Word: ", " ".join(hidden_word))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet_letters - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is not in the word!")
        elif user_letter in used_letters:
            print(f"You have already used the letter, {user_letter}, Try again!")
        else:
            print("Invalid Character, Try again!")

    hidden_word = [letter if letter in used_letters else "_" for letter in word]
    print("Current Word: ", " ".join(hidden_word))
    if lives == 0:
        print("You Died!")
    else:
        print("Congratulation, You Won!")

hangman()