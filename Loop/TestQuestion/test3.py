# Number guessing game
import random
print("Welcome to the number guessing game!")
number_to_guess = random.randint(1, 100)
guess = None
while guess != number_to_guess:
    guess = int(input("Guess the number: "))
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess} correctly!")