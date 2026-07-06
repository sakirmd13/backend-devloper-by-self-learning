#Function
# A function is a block of code that performs a specific task. It can take inputs, process them, and return an output.

# 1: Basic Function
# A basic function is defined using the def keyword, followed by the function name and parentheses. The code block within the function is indented.


# Function Names
# Function names follow the same rules as variable names in Python:

# A function name must start with a letter or underscore
# A function name can only contain letters, numbers, and underscores
# Function names are case-sensitive (myFunction and myfunction are different)

# Why Use Functions?

# Functions help organize code into reusable blocks, making it easier to read, maintain, and debug. They also allow for modular programming, where different parts of a program can be developed and tested independently.

# Example 1: A basic function that prints a greeting message
def greet():
    print("Hello, World!")
    
greet()  # Output: Hello, World!


# 2: Function with Parameters
# Functions can take parameters, which are values passed into the function to customize its behavior.

# Example 2: A function that takes a name as a parameter and prints a personalized greeting
def greet(name):
    print(f"Hello Coder: {name}!")
    
name=input("Enter your name: ")
greet(name) # the function greet is called with the name variable as an argument, and the personalized greeting is printed

#What is return?
# The return statement is used to exit a function and pass a value back to the caller.

#Example 3: A function that takes two numbers as parameters and returns their sum
def add_numbers(num1,num2):
    return num1 + num2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = add_numbers(num1, num2) #the function add_numbers is called with num1 and num2 as arguments, and the result is stored in the variable sum
print(f"The sum of {num1} and {num2} is: {sum}")


# 3: A function that takes a list of numbers as a parameter and returns the average
def calculate_average(numbers):
    if len(numbers)==0:
        return 0
    return sum(numbers) / len(numbers) #the function calculate_average is defined to take a list of numbers as a parameter. It first checks if the list is empty (length is 0). If it is empty, it returns 0 to avoid division by zero. Otherwise, it calculates the average by summing the numbers in the list and dividing by the length of the list. The result is then returned.

numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers) #the function calculate_average is called with the numbers list as an argument, and the result is stored in the variable average
print(f"The average of the numbers is: {average}") #because the list is not empty, the average is calculated and printed

# 4: A function that takes a string as a parameter and returns the number of vowels in the string
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

string = input("Enter a string: ")
vowel_count = count_vowels(string) #the function count_vowels is called with the string variable as an argument, and the result is stored in the variable vowel_count
print(f"The number of vowels in the string is: {vowel_count}") #the number of vowels in the string is calculated and printed


#Functions with Default Parameters
# In Python, you can define default values for function parameters. If the caller does not provide a value for that parameter, the default value will be used.
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
    
greet("Alice")  # Output: Hello, Alice!
greet("Bob", "Hi")  # Output: Hi, Bob!

#What is *args?
# In Python, *args is used to pass a variable number of positional arguments to a function. It allows you to pass any number of arguments to the function, which are then accessible as a tuple within the function.


#Functions with Variable-Length Arguments (*args and **kwargs)
# In Python, you can define functions that accept a variable number of arguments using *args for positional arguments and **kwargs for keyword arguments.

#Example 1: A function that takes a variable number of positional arguments and prints them
def print_numbers(*args):# The *args parameter allows the function to accept any number of positional arguments. Inside the function, args is treated as a tuple containing all the passed arguments. The function then iterates over each number in args and prints it.
    for number in args:
        print(number)

print_numbers(1, 2, 3, 4, 5)


#Using *args with Regular Arguments
# In Python, you can use *args in combination with regular arguments in a function definition. The regular arguments must come before *args in the parameter list.
#Example 1: A function that takes a regular argument and a variable number of positional arguments
def print_values(regular_arg, *args):
    print(f"Regular Argument: {regular_arg}")
    for value in args:
        print(value)
    
print_values("Regular", 1, 2, 3, 4, 5)

#What is **kwargs?
# In Python, **kwargs is used to pass a variable number of keyword arguments to a function. It allows you to pass any number of named arguments to the function, which are then accessible as a dictionary within the function.

#Example 2: A function that takes a variable number of keyword arguments and prints them
def print_info(**kwargs):# The **kwargs parameter allows the function to accept any number of keyword arguments. Inside the function, kwargs is treated as a dictionary containing all the passed keyword arguments. The function then iterates over each key-value pair in kwargs and prints them.
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
print_info(name="Alice", age=30, city="New York")

# Using **kwargs with Regular Arguments
# In Python, you can use **kwargs in combination with regular arguments in a function definition. The regular arguments must come before **kwargs in the parameter list.
#Example 2: A function that takes a regular argument and a variable number of keyword arguments

def print_detail(regular_arg, **kwargs):
    print(f"Regular Argument: {regular_arg}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_detail("Regular", name="Alice", age=30, city="New York")
       


#Example 3: A function that takes both variable-length positional and keyword arguments
def print_details(*args, **kwargs):# The function print_details is defined to accept both variable-length positional arguments (*args) and variable-length keyword arguments (**kwargs). Inside the function, it first prints the positional arguments by iterating over args. Then, it prints the keyword arguments by iterating over the key-value pairs in kwargs.
    print("Positional Arguments:")
    for arg in args:
        print(arg)


    
    print("\nKeyword Arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(1, 2, 3, name="Alice", age=30, city="New York")



#Unpacking Arguments
# In Python, you can unpack arguments from a list or dictionary when calling a function. This allows you to pass multiple values to a function without explicitly specifying each argument.
#Example 1: Unpacking a list of arguments
def print_numbers(num1, num2, num3):
    return num1*num2+num3

numbers=[2,4,6]

result=print_numbers(*numbers)
print(result)


#function with keyword-only arguments
# In Python, you can define functions that accept keyword-only arguments by placing a * in the function definition. Any parameters defined after the * must be specified using keyword arguments when calling the function.

#Example 1: A function that takes keyword-only arguments
def print_info(*, name, age, city):# The * in the function definition indicates that all parameters following it must be specified as keyword arguments. The function print_info takes three keyword-only arguments: name, age, and city. Inside the function, it prints the values of these arguments.
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    
print_info(name="Alice", age=30, city="New York")  # Output: Name: Alice, Age: 30, City: New York   


#Positional Arguments
# In Python, you can define functions that accept positional arguments. Positional arguments are passed to the function based on their position in the argument list.
#Example 1: A function that takes positional arguments
def print_info(name, age, city):# The function print_info is defined to accept three positional arguments: name, age, and city. Inside the function, it prints the values of these arguments.
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    
print_info("Alice", 30, "New York")  # Output: Name: Alice, Age: 30, City: New York



#Mixing Positional and Keyword Arguments
# In Python, you can mix positional and keyword arguments when calling a function. Positional arguments must come before keyword arguments in the argument list.
#Example 1: A function that takes both positional and keyword arguments
def print_info(name, age, city):# The function print_info is defined to accept three parameters: name, age, and city. Inside the function, it prints the values of these parameters.
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
print_info("Alice", age=30, city="New York")  # Output: Name: Alice, Age: 30, City: New York


#functions can also be nested, meaning you can define a function inside another function. The inner function can access variables from the outer function's scope.
#Example 4: A function that defines another function inside it
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

print(outer_function(5)(10))  # Output: 15
# in this example, outer_function takes a parameter x and defines an inner function inner_function that takes a parameter y. The inner function returns the sum of x and y. When outer_function is called with the argument 5, it returns the inner_function. Then, calling the returned inner_function with the argument 10 results in the sum of 5 and 10, which is 15.

print(outer_function(5))#output: <function outer_function.<locals>.inner_function at 0x7f8c8c8c8c10> because outer_function(5) returns the inner_function, which is a function object. The output shows the memory address of the inner_function, indicating that it is a function that can be called later.


#Returning Different Data Types
# In Python, functions can return different data types, including numbers, strings, lists, dictionaries, and even other functions. The return type of a function is determined by the value returned by the return statement.
#Example 5: A function that returns a list of even numbers from a given range
def get_even_numbers(start, end):
    even_numbers = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

even_numbers = get_even_numbers(1, 10) #the function get_even_numbers is called with the arguments 1 and 10, and the result is stored in the variable even_numbers
print(f"Even numbers from 1 to 10: {even_numbers}") #the list of even numbers from 1 to 10 is calculated and printed



#Positional-Only Arguments
# In Python, you can define functions that accept positional-only arguments by placing a / in the function definition. Any parameters defined before the / must be specified using positional arguments when calling the function.
#Example 1: A function that takes positional-only arguments
def print_info(name, age, city, /):# The / in the function definition indicates that all parameters before it must be specified as positional arguments. The function print_info takes three positional-only arguments: name, age, and city. Inside the function, it prints the values of these arguments.
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

print_info("Alice", 30, "New York")  # Output: Name: Alice, Age: 30, City: New York


#Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

#Example 2: A function that takes positional arguments without the / and allows keyword arguments
def print_info(name, age, city):# The function print_info is defined to accept three parameters: name, age, and city. Inside the function, it prints the values of these parameters.
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

print_info(name="Alice", age=30, city="New York")  # Output: Name: Alice, Age: 30, City: New York



#Combining Positional-Only and Keyword-Only
# In Python, you can define functions that accept both positional-only and keyword-only arguments by using both / and * in the function definition. Parameters before the / must be specified as positional arguments, while parameters after the * must be specified as keyword arguments.

#Example 1: A function that takes both positional-only and keyword-only arguments
def print_info(name, age, /, *, city):# The function print_info is defined to accept one positional-only argument (name), one positional argument (age), and one keyword-only argument (city). Inside the function, it prints the values of these arguments.
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    
print_info("Alice", 30, city="New York")  # Output: Name: Alice, Age: 30, City: New York



#Scope
#In Python, scope refers to the region of a program where a variable can be accessed. Python follows the LEGB rule to determine variable scope:

# L – Local Scope: Variables defined inside a function.
# E – Enclosing Scope: Variables in the outer function when functions are nested.
# G – Global Scope: Variables defined at the top level of a module.
# B – Built-in Scope: Names that are predefined by Python, such as print(), len(), etc.


# 1. Local Scope

# A variable created inside a function is only accessible within that function.

def greet():
    message = "Hello"
    print(message)

greet()
# print(message)  # Error: message is not defined



# 2. Global Scope

# A variable defined outside all functions is global and can be accessed anywhere in the module.

name = "Alice"

def show():
    print(name)

show()   # Output: Alice
print(name)  # Output: Alice


# 3. Enclosing Scope

# Used in nested functions. The inner function can access variables from the outer function.
# def outer():
#     x = 10

#     def inner():
#         print(x)

#     inner()

# outer()   # Output: 10


# 4. Built-in Scope

# Python provides built-in functions and names that are always available.

numbers = [1, 2, 3]
print(len(numbers))  # len() is a built-in function


# Using global

# To modify a global variable inside a function, use the global keyword.

count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # Output: 1

# Using nonlocal

# To modify a variable in the enclosing scope, use the nonlocal keyword.
def outer():
    x = 5

    def inner():
        nonlocal x
        x += 1
        print(x)

    inner()

outer()  # Output: 6


# Python searches for a variable in this order: Local → Enclosing → Global → Built-in (LEGB).


# Naming Variables
# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):


# Example
# The function will print the local x, and then the code will print the global x:

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)