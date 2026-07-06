#Python Booleans
# In Python, booleans represent truth values and have two possible values:
# True and False. They are often used in conditional statements and logical operations.and get one of two answers, True or False. Booleans are a fundamental data type in Python and are used to control the flow of a program based on certain conditions.

#Example 1:
is_sunny = True
is_raining = False
print("Is it sunny today?", is_sunny)  # Output: Is it sunny today? True
print("Is it raining today?", is_raining)  # Output: Is it raining today? False
print(f"Is it sunny and not raining? {is_sunny and not is_raining}")  # Output: Is it sunny and not raining? True
print(type(is_sunny))  # Output: <class 'bool'>
print(type(is_raining))  # Output: <class 'bool'>


#Example 2: with user input statement
name=input("Enter your name: ")
print(f"Hello, {name}!")
for n in name:
    if n=='a':
        n=True
        print(f"Found an 'a' in your name: {n}")
    else:
        n=False
        print(f"No 'a' found in this character: {n}")
        
 
#Example 3: Check if a number is positive or negative       
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
    is_positive = True
else:
    print("The number is not positive.")
    is_positive = False


#Evaluate Values and Variables

#In Python, you can use the bool() function to evaluate any value or variable. It returns either:
# True → If the value is considered truthy
# False → If the value is considered falsy
#1 its considered truthy
#0 its considered falsy



#Most Values are True
# In Python, most values evaluate to True when passed to the bool() function.
# In general, any value that has some content or is non-zero is considered True.

#Example 4:
print(bool(1))  # Output: True because 1 is a non-zero number 1 its considered truthy
print(bool(True))  # Output: True
print(bool([1, 2, 3]))  # Output: True because the list is not empty
print(bool("Hello"))  # Output: True because the string is not empty
print(bool({"key": "value"}))  # Output: True because the dictionary is not empty
print(bool({1, 2, 3}))  # Output: True because the set is not empty
print(bool(3.14))  # Output: True because 3.14 is a non-zero number
print(bool(-1))  # Output: True because -1 is a non-zero number



# Some Values are False
# In Python, some values always evaluate to False when passed to the bool() function. These values are called Falsy Values.

# A value is usually False if it is:
# Empty
# Zero
# None
# The boolean value False


#Example 5:
print(bool(0))  # Output: False because 0 is a zero number 0 its considered falsy
print(bool("")  )# Output: False because the string is empty
print(bool([]))  # Output: False because the list is empty
print(bool(None))  # Output: False because None is considered falsy
print(bool(False))  # Output: False
print(bool({}))  # Output: False because the dictionary is empty
print(bool(set()))  # Output: False because the set is empty
print(bool(0.0))  # Output: False because 0.0 is a zero number


# Functions can Return a Boolean
# In Python, functions can return boolean values (True or False) based on certain conditions. This allows you to create custom logic and make decisions in your code.

#Example 6: A function that checks if a number is even or odd
def is_even(number):
    return number % 2 == 0

number = int(input("Enter a number to check if it's even: "))
print(is_even(number))  # Output: True if the number is even, False otherwise


#Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

#The isinstance() function is a built-in Python function used to check whether an object belongs to a specific class (data type). It returns:

# True → If the object is an instance of the specified class.
# False → Otherwise.

#Example 7:
print(isinstance(5, int))  # Output: True
print(isinstance("Hello", str))  # Output: True