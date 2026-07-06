# Decorators in Python

# A decorator is a function that takes another function (or class) as input, adds some functionality, and returns the modified function without changing its original code.


def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def greet():
    print("Hello!")

greet()


#By placing @decorator directly above the function definition, the function greet is being "decorated" with the decorator function.

#Multiple Decorator Calls
# A decorator can be called multiple times. Just place the decorator above the function you want to decorate.
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())

# The line: @decorator is equivalent to: greet = decorator(greet)

# Decorator with Arguments

# To handle functions that accept parameters, use *args and **kwargs:

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        result = func(*args, **kwargs)
        print("Function execution completed")
        return result
    return wrapper

@decorator
def add(a, b):
    return a + b

print(add(3, 5))


def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("Your Name! "))


# Preserving Function Metadata

# Use functools.wraps to keep the original function's name and docstring:

from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Running...")
        return func(*args, **kwargs)
    return wrapper


#Decorator with Parameters
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi() 


# Preserving Function Metadata
# Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.

# Normally, a function's name can be returned with the __name__ attribute:

def myfunction():
  return "Have a great day!"

print(myfunction.__name__)
# But, when a function is decorated, the metadata of the original function is lost.




# Try returning the name from a decorated function and you will not get the same result:

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)


#o fix this, Python has a built-in function called functools.wraps that can be used to preserve the original function's name and docstring.


# Import functools.wraps to preserve the original function name and docstring.

import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)