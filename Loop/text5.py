#Number multiplication addition subtraction division modulo pi game using while loop with if, elif, else, break, continue, pass statements and nested loop with a nested loop and break statement and continue statement and pass statement and else clause and user input
import random
import math
print("Welcome to the number operations game!")
print("You will be given two random numbers and you need to perform addition, subtraction, multiplication, division, and modulo operations.")
score=0
total_questions=0
operations = ['+', '-', '*', '/', '%']
while True:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(operations)
   
    
    # Perform the operation based on the random choice
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2
    elif operation == '/':
        num2 = random.randint(1, 100)  # Ensure num2 is not zero for division
        while num2 == 0:
            num2 = random.randint(1, 100)
        correct_answer = num1 / num2
    elif operation == '%':
        correct_answer = num1 % num2
    
    total_questions += 1
    user_answer = float(input(f"question {total_questions}: What is {num1} {operation} {num2}? "))
    if user_answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break

print(f"Game over! Your score is {score}/{total_questions}.")
print("Thank you for playing the number operations game!")
