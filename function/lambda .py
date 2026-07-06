#Lambda Functions
# A lambda function in Python is a small, anonymous function defined using the lambda keyword. It is useful when you need a simple function for a short period of time.

#Syntax
# lambda arguments: expression

# arguments → Input parameters.
# expression → A single expression whose result is returned automatically.

#1. Add two numbers
add = lambda a, b: a + b

print(add(5, 3))

#2. Square a number
square = lambda x: x * x

print(square(4))

#3. Find the larger number
maximum = lambda a, b: a if a > b else b

print(maximum(10, 20))



# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def myfunc(n):
  return lambda a : a * n

# Use that function definition to make a function that always doubles the number you send in:


#4. Using lambda with sorted()
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78)
]

sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)

# 5. Using lambda with map()
numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x * x, numbers))

print(squares)

# 6. Using lambda with filter()
numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)


# Lambda vs Normal Function

# Normal function
def add(a, b):
    return a + b

print(add(2, 3))

# Lambda function
add = lambda a, b: a + b

print(add(2, 3))




# When to use lambda
#  For short, simple functions.
#  As arguments to functions like map(), filter(), and sorted().
#  Avoid for complex logic—use a regular def function instead, since it is easier to read and maintain.

# Key points:

# Anonymous (no def required).
# Can have any number of arguments.
# Contains only one expression (no multiple statements or loops).
# Automatically returns the value of that expression.