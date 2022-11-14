# randomnumbergame.py
# COCP 1213 Midterm: Chapter 3.2 While Loop Project
# A program where the user guesses a random number between 1 and 10, and is presented with two of their previous guesses (if they guessed twice) and a congratulations if they guessed correctly.
# By: Noelle Robertson

# Import random number generator.
import random
random_number = random.randint(1, 10)
# print(random_number)

# Ask for the user to pick a number between 1 and 10. Create a variable for a wrong input. End the program if they guess the random number on the first try.
guess = int(input("Guess a number between 1 and 10: "))
if guess != random_number:
    wrong_guess = guess
if guess == random_number:
    print()
    print("Yay! You picked the random number on your first try!")
    print("The random number was: ", random_number)
    quit()

# Create a loop that continues to ask the user to pick a number until they hit the random number.
while guess != random_number:
    wrong_again = guess
    if guess > 10:
        guess = int(input("Your guess was out of bounds. \nPlease pick a number between 1 and 10: "))
    if guess > random_number:
        guess = int(input("Too high! \nPlease pick a number between 1 and 10: "))
    if guess < random_number:
        guess = int(input("Too low! \nPlease pick a number between 1 and 10: "))

# Print the congratulations, two previous guesses and the random number.
else:
    print()
    print("Yay! You picked the random number!")
    print("Your previous guesses were: ", wrong_guess, wrong_again)
    print("The random number was: ", random_number)
