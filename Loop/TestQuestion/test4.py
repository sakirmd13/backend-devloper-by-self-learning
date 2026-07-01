#Number adding game using while loop with if, elif, else, break, continue, pass statements and nested loop with a nested loop and break statement and continue statement and pass statement and else clause and user input

import random


while True:
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)
    print(f"Add the following numbers: {number1} + {number2}")
    result = int(input("What is the sum? "))
    
    
    if result == number1 + number2:
        print("Correct!")
    else:
        print("Incorrect!")
    
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break



