# User will be given 6 guesses to guess a randomly chosen number.

import random, inputValidator
nGuess = 6
nGuessLeft = nGuess
correctGuess = random.randint(1,20)
print("I am thinking of a number between 1 and 20.")
print("You have 6 tries to guess the number correctly.")
guess = input("What is your guess?\n")
for i in range(nGuess):
    nGuessLeft = nGuessLeft - 1  
    while not inputValidator.isInteger(guess):
        guess = input("Please enter an integer.\n")
    guess = int(guess)
    if guess == correctGuess:
        print("Congrats! You got it!")
        break
    elif guess < correctGuess:
        print("That's a bit low.",end=" ")
    else:
        print("That's a bit high.",end=" ")
    if nGuessLeft > 1:
        guess = input("You have "+str( nGuessLeft )+" guesses left!\n")
    elif nGuessLeft ==1:
        guess = input("You have "+str( nGuessLeft )+" guess left!\n")
    else:
        print("\nYou are out of guesses!\nThe correct number was "+str ( correctGuess )+".")
