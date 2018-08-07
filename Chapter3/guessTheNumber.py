# User will be given 6 guesses to guess a randomly chosen number.

import random, inputValidator
nGuess = 6
nGuessLeft = nGuess
correctGuess = random.randint(1,20)
print("I am thinking of a number between 1 and 20.")
print("You have 6 tries to guess the number correctly.")
for numTry in range(nGuess):
    guess = input("What is your guess?\n")
    while not inputValidator.isInteger(guess):
        guess = input("Please enter an integer.\n")
    nGuessLeft = nGuessLeft - 1  
    guess = int(guess)
    if guess < correctGuess:
        print("That's a bit low.",end=" ")
    elif guess > correctGuess:
        print("That's a bit high.",end=" ")
    else:
        break
    if nGuessLeft > 1:
        guess = print("You have "+str( nGuessLeft )+" guesses left!\n")
    elif nGuessLeft ==1:
        guess = print("You have "+str( nGuessLeft )+" guess left!\n")
if guess == correctGuess:
    if numTry > 1:
        print("Congrats! You got it in "+str(numTry)+ " guesses!")
    else:
        print("Amazing! You got it in a single shot! (Are you a psychic?)")
else:
    print("\nYou are out of guesses!\nThe correct number was "+str ( correctGuess )+".")
