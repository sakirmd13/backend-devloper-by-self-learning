#User Input
#In Python, user input is used to accept data from the keyboard while the program is running. Python provides the built-in input() function for this purpose.
#The input() function always returns the input as a string.



#Example 1: Simple Input
name=input("Enter your Name:")
print(name)

#Example 2: Taking a Number as Input
# Since input() returns a string, you need to convert it to a number.
age=int(input("Enter your Age:"))
print(age)


#Example 3: Taking a Decimal Number
height=float(input("Enter your Height:"))
print(height)


#Example 4: Multiple Inputs
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Name:", name)
print("Age:", age)

#Example 5: Taking Multiple Values in One Line
a, b = input("Enter two numbers: ").split()

print("First:", a)
print("Second:", b)


#If you want them as integers:
a, b = map(int, input("Enter two numbers: ").split())
print("Sum =", a + b)

#Type Conversion with input()
# | Function  | Converts Input To                | Example                  |
# | --------- | -------------------------------- | ------------------------ |
# | `str()`   | String                           | `name = input()`         |
# | `int()`   | Integer                          | `age = int(input())`     |
# | `float()` | Decimal                          | `price = float(input())` |
# | `bool()`  | Boolean (rarely used with input) | `flag = bool(input())`   |


# Key Points
# input() reads data from the keyboard.
# It always returns a string.
# Use int(), float(), or other conversion functions when numeric input is needed.
# You can display a prompt inside input() to guide the user.

# For beginners, the most common pattern is:
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name)
print("Next year you will be", age + 1)
#This example combines string input, integer conversion, and output in one simple program.



#f-String in Python
#An f-string (formatted string literal) is a simple and efficient way to insert variables and expressions into a string. It was introduced in Python 3.6.

# Syntax
# f"Text {variable}"

# Prefix the string with f or F.
# Place variables or expressions inside curly braces {}.

# Example 1: Using a Variable
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name}, and I am {age} years old.")

#Example 2: Expressions
# You can perform calculations inside {}
a = 10
b = 20

print(f"Sum = {a + b}")
print(f"Product = {a * b}")


# Example 3: Formatting Numbers

pi = 3.14159265

print(f"Pi = {pi:.2f}")
# Here:(.2f) means display the number with 2 digits after the decimal point.

#Example Formatting Integers
num = 7

print(f"{num:03}")
#This pads the number with zeros until it has 3 digits.


#Example Aligning Text
name = "Python"

print(f"|{name:<10}|")  # Left align
print(f"|{name:^10}|")  # Center align
print(f"|{name:>10}|")  # Right align



#Why Use f-Strings?
# Instead of writing:
name = "Alice"
age = 25

print("Name:", name, "Age:", age)
print("Name: {} Age: {}".format(name, age))
print(f"Name: {name}, Age: {age}")


# This is:Easier to read
# Shorter to write
# Faster than older formatting methods


# Summary
# | Syntax          | Meaning                |
# | --------------- | ---------------------- |
# | `f"{name}"`     | Insert a variable      |
# | `f"{a + b}"`    | Evaluate an expression |
# | `f"{pi:.2f}"`   | Show 2 decimal places  |
# | `f"{num:03}"`   | Pad with leading zeros |
# | `f"{text:<10}"` | Left align text        |
# | `f"{text:^10}"` | Center align text      |
# | `f"{text:>10}"` | Right align text       |

# Remember: Always prefix the string with f (or F), otherwise anything inside {} will be treated as normal text rather than evaluated.
