import math
import random
number = random.randrange(1,100)
chances = 7
print("Hello and welcome to the random number guessing game!")
print("You have",chances, "chances to guess the correct number I generate,")
print("Good Luck!")

#print(number)
gameOver = 0
attempts = 0
badGuess = []
while chances > 0:
    print("You have",chances,"guesses remaining!")
    guess = int(input("Enter a whole number between 1 - 100:"))
    badGuess.append(guess)
    print("Past guesses are",badGuess,":")
    if guess > number:
        print("Your number is too high!")
        chances = chances - 1
        gameOver = 1
        attempts = attempts + 1
    elif guess < number:
        print("Your number is low!")
        chances = chances - 1
        gameOver = 1
        attempts = attempts + 1
    elif guess == number:
        attempts = attempts + 1
        print("Congragulations you have guessed correctly!")
        print("It took you",attempts,"guesses!")
        chances = 0
        gameOver = 0

if gameOver == 1:
    print("You have been defeated, my number was",number,"!")
    print("Please, try your luck again!")
else:
    print("Please play again!")
