# This is a guess the number game.
import random
from random import randint
import time
import os


#For clearing the terminal
if __name__ == '__main__':
	clear = lambda: os.system('cls')

	clear()

#Game Instructions

print('This is a guess the number game.')
time.sleep(2)
print('In this game you will be given 6 chances to take the correct guess of the number the game has selected between 1 to 20.')
time.sleep(4)
print('If you take the correct guess within the chances...You Win, else you will Lose.')
time.sleep(3)
print('I hope you understood the instructions..')
time.sleep(2)
print("So let's start the game.") 
time.sleep(3)

#Guess taken meter
guessesTaken = 0

#Taking user name as Input
myName = input("\nHello! What's your name: ")

#Assigning a variable for selecting a random number between 1 to 20
x = random.randint(1,20)

print('Well ' + myName + ', I have choosen a number between 1 and 20.\nNow You have to guess it.',x)

#While loop for playing the game until maximum guesses are reached

while True:

    print('Take a guess.')              #For taking the guess

    try:                                #For integer number as guesses
        
        guess = int(input())
    
    except ValueError:                  #If user enters a non integer value this will get printed
        
        print("Invalid Input..\nTry again later...")
        exit()
    
    guessesTaken = guessesTaken + 1         #For adding the guesses as guess is taken

    #If conditions for checking whether the guess is correct or not

    if guess != x:                     

        x = str(x)
        print("Nope.That's the wrong number...Try again!")


    if x == guess:
        
        guessesTaken = str(guessesTaken)
        
        print('Congractulations, ' + myName + '! You guessed my number.')
        time.sleep(3)
        print("Thanks for playing.")
        time.sleep(2)
        break

    #If condition for checking if the maximum number of guesses are taken
    
    if guessesTaken >= 6:
        print("Sorry You Lost! As you are out of chances...")
        time.sleep(2)
        print("Please try again...")
        time.sleep(2)
        print("Thanks for playing...")
        time.sleep(2)
        exit()