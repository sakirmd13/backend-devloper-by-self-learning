#Python Casting

# Python Casting means converting one data type into another. Python provides built-in functions for this purpose.

# Why is Casting Needed?

# Sometimes you need to convert data from one type to another before performing operations.

# For example:

# Convert a string to an integer for calculations.
# Convert an integer to a string for printing.
# Convert a float to an integer by removing the decimal part.



#Common Casting Functions
# | Function| Converts To | Example                |
# | --------| ----------- | ---------------------- |
# | int()   | Integer     | `int("10")` → `10`     |
# | float() | Float       | `float("10")` → `10.0` |
# | str()   | String      | `str(10)` → `"10"`     |
# | bool()  | Boolean     | `bool(1)` → `True`     |


#1. Casting to Integer (int())
x = 5.9
y = "20"

print(int(x))
print(int(y))

#Note: int() removes the decimal part (it does not round).

#2. Casting to Float (float())
x = 10
y = "15.7"

print(float(x))
print(float(y))
#Note float() add 0

#3. Casting to String (str())
age = 25

print(str(age))
print(type(str(age)))


#4. Casting to Boolean (bool())
# Python considers some values as False and others as True.

print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Hello"))



# Values that become False
# 0
# 0.0
# "" (empty string)
# [] (empty list)
# () (empty tuple)
# {} (empty dictionary)
# set()
# None

# Everything else becomes True.


#Example: String to Integer
num1 = "10"
num2 = "20"

result = int(num1) + int(num2)

print(result)

#Without casting:
num1 = "10"
num2 = "20"

print(num1 + num2)
#This is because strings are concatenated, not added.

# Invalid Casting
# Not every value can be converted.

# x = "Hello"
# print(int(x))

#ValueError: invalid literal for int() with base 10: 'Hello'


# Key points to remember:

# int() converts to an integer and truncates any decimal part.
# float() converts to a floating-point number.
# str() converts any value into a string.
# bool() converts values to True or False based on whether they are considered truthy or falsy.