#Python Numbers

#-> There are three numeric types in Python:

# int
# float
# complex

# Variables of numeric types are created when you assign a value to them:


# Int
# -> Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
num1=1234
num2=-3456
num3=1234567890

print(num1)
print(num2)
print(num3)



# Float
# -> Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
num4=1.3
num5=-11.11

print(num4)
print(num5)

#In Python, the e in a number represents scientific notation (also called exponential notation). It means "× 10 to the power of".

num6=-12.3e2
print(num6)



num7=12.3e2345 #inf
print(num7)
#This is an extremely large number. Since Python's float type follows the IEEE 754 standard, it cannot represent numbers anywhere near 10^2345. As a result, the value overflows and becomes:
#inf means negative infinity


#Complex
# -> Complex numbers are written with a "j" as the imaginary part:

num8=1+2j
print(num8)



#Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:


print(float(num1))
print(int(num5))


#Note: You cannot convert complex numbers into another number type.


#Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

import random
print(random.randrange(2,8))