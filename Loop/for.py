#For Loop
#A for loop in Python is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item

#This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# Syntax
# for variable in sequence:
    # Code to execute
  
#Example 1: Iterating over a list  
fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print(f)
    
# The for loop does not require an indexing variable to set beforehand.



#Looping Through a String
#A string is a sequence of characters. You can use a for loop to access each character one by one
#Example 2: Iterating through a string
for letter in "banana":
    print(letter)
    

#Example 3: Iterating through a string using a variable 
name="John"
for n in name:
    print(n)
    
    
    
#The break Statement
#The break statement is used to immediately terminate (stop) a loop when a specific condition is met. Once break is executed, the loop ends and the program continues with the first statement after the loop

# Syntax
# for variable in sequence:
#     if condition:
#         break
    # Other statements
    
    
#Flow Diagram
# Start
#    │
#    ▼
# Loop Starts
#    │
#    ▼
# Condition True?
#    │
#  ┌─┴─────────┐
#  │           │
# Yes         No
#  │           │
#  ▼           ▼
# break    Execute Code
#  │           │
#  ▼           │
# Exit Loop ◄──┘
#    │
#    ▼
# Next Statement

#Example 4: Using break in a for loop
fruits = ["apple", "banana", "cherry"]
for f in fruits:
    if f == "banana":
        break
    print(f)
    
#Example 5: Using break in a for loop with a string
for letter in "banana":
    if letter == "n":
        break
    print(letter)


#The continue Statement
#The continue statement is used to skip the current iteration of a loop and move on to the next iteration. When continue is executed, the rest of the code inside the loop for that iteration is skipped, and the loop proceeds to the next item in the sequence.


# Flow Diagram
# Start
#    │
#    ▼
# Loop Starts
#    │
#    ▼
# Condition True?
#    │
#  ┌─┴─────────┐
#  │           │
# Yes         No
#  │           │
#  ▼           ▼
# Skip Current  Execute Code
# Iteration     │
#  │            │
#  └──────► Next Iteration


#Example 6: Using continue in a for loop

# Syntax
# for variable in sequence:
#     if condition:
#         continue
    # Code to execute
    
    
fruits = ["apple", "banana", "cherry"]
for f in fruits:
    if f == "banana":
        continue
    print(f)
    
#Example 7: Using continue in a for loop with a string
name="your name"
for n in name:
    if n=="":
        continue
    print(n)
    
##The range() Function
#The range() function is used to generate a sequence of numbers. It is commonly used in for loops to specify the number of iterations. The range() function can take one, two, or three arguments:

#Range with one argument: range(stop) generates numbers from 0 to stop-1.
#Example: range(5) generates 0, 1, 2, 3, 4.
for n in range(5):
    print(n)

# Note that range(5) is not the values of 0 to 4, but the values 0 to 5
    
#Example 8: Using range(start, stop) with two arguments
for n in range (3,9):
    print(n)
    
    
#Example 9: Using range(start, stop, step) with three arguments
for n in range (2, 10, 2):
    print(n)
    
    
#Else in For Loop
#In Python, the else block can be used in conjunction with a for loop. The else block is executed after the for loop completes its iteration over the sequence, but only if the loop was not terminated by a break statement. If the loop is exited prematurely using break, the else block will be skipped.

numbers=[1, 2, 3, 4, 5]
for n in numbers:
    print(n)
else:
    print("Loop completed without encountering a break statement.")
    
    
for n in range(1,6):
    if n == 3:
        print(f"Found the number {n}, exiting the loop.")
        break
    print(n)
else:
    print("Loop completed without encountering a break statement.")
    
    
#Nested For Loops
#A nested for loop is a loop inside another loop. The inner loop will be executed one time for each iteration of the outer loop. Nested loops are often used to work with multi-dimensional data structures, such as lists of lists or matrices.


#Example 10: Using nested for loops
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"i: {i}, j: {j}")
        
#Example 11: using nested loop print stars in a pattern
rows = 5
for i in range(1,rows+1):
    for  j in range(1,i+1):
        print("*", end="")
    print("")  # Move to the next line after each row

    
#Example 12: using nested loop print numbers in a pattern of triangle
rows = 5
for i in range (1,rows+1):
    for j in range (1,i+1):
        print(j,end=" ")# Print numbers in the same row with a space
    print(" ")# Move to the next line after each row
    
    
#Example 13: using nested loop print numbers in a pattern of pyramid 

#     1
#    12
#   123
#  1234
# 12345
rows = 5
for i in range(1,rows+1):
    for  j in range(1,rows-i+1):# Print spaces for alignment
        print(" ",end="")# Print spaces for alignment
    for k in range(1,i+1):# Print numbers in the same row
        print(k,end="")# Print numbers in the same row without space
    print(" ")# Move to the next line after each row
    
    
 #Example 14: using nested loop print numbers in a pattern of pyramid with spaces 
#          1
#       1 2 3
#     1 2 3 4 5
#   1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8 9  

rows = 5

for i in range(1, rows + 1):# Loop through each row
    # Print leading spaces
    for j in range(rows - i):# Print spaces for alignment
        print("  ", end="")# Print two spaces for better alignment

    # Print numbers
    for k in range(1, 2 * i):# Print numbers in the same row
        print(k, end=" ")# Print a space after each number for better readability

    print()# Move to the next line after each row
    



#The pass Statement
#The pass statement is a null operation; it does nothing when executed. It is used as a placeholder in situations where a statement is syntactically required but you do not want to execute any code. This can be useful for creating minimal classes, functions, or loops that you plan to implement later.
for i in range(5):
    pass  # Placeholder for future code
