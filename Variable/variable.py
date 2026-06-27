# What is variable in python
# ->Variables are containers for storing data values.


# How we can create a variable 
# -> To create a variable in Python, you simply type the variable name and assign a value to it using the = operator
# -> Python has no special command or keyword to declare a variable. The variable is automatically created the exact moment you assign it a value for the first time

# The variable 'age' is created and assigned the integer 25
age = 25 
print(age)

# The variable 'string' is created and assigned the string "Your Name"
name="Your name "
print(name)


# 5 Strict Naming Rules

#When naming your variables, you must follow these absolute rules to avoid syntax errors

# 1) Start with a letter or underscore: A name must start with a letter (a-z, A-Z) or an underscore (_).

# 2) No leading numbers: A variable name cannot start with a digit (e.g., 1user is invalid).

# 3) Allowed characters: Names can only contain alphanumeric characters and underscores (A-z, 0-9, and _).

# 4) Case-sensitivity: Variable names are case-sensitive (age, Age, and AGE are three separate variables).

# 5)No reserved keywords: You cannot use Python's built-in keywords (such as if, else, for, def, or class) as names.


#Examples of Names

# Valid Names: 
user_id=1
_database_connection=True
totalAmount2=200
X="y"

print(user_id,_database_connection,totalAmount2,X)
#Invalid Names: 

# 2user (starts with a number), user-id (contains a hyphen), user id (contains a space), global (reserved keyword).


# Key Characteristics

# 1) Dynamic Typing: You do not need to specify data types. Python automatically detects if a value is a string, integer, or float, and you can reassign the variable to a different type later.

# 2) Snake Case Convention: While not a strict rule, Python's official styling guide recommends using lowercase words separated by underscores (user_name) for multi-word variables to maintain clean code readability



# Casting

# -> if you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)

# Get the Type

# ->You can get the data type of a variable with the type() function.

age=5

print(age)
print(type(age))


name="Your name"

print(name)
print(type(name))



# Single or Double Quotes?

#-> String variables can be declared either by using single or double quotes:

name="Your name"
print(name)

Name='Your City'
print(Name)




# Many Values to Multiple Variables

# -> Python allows you to assign values to multiple variables in one line

# -> Note: Make sure the number of variables matches the number of values, or else you will get an error.
a,b,c="Apple","Banana",23

print(a)
print(b)
print(c)


#One Value to Multiple Variables

# -> And you can assign the same value to multiple variables in one line:

a=b=c="Your Name"

print(a)
print(b)
print(c)


#Unpack a Collection

# -> If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

city=["Samastipur","Patna","Gaya"]
a,b,c=city

print(a)
print(b)
print(c)



#Output Variables

# -> The print() function is often used to output variables

title="Python is Funtastic Programming Language"
print(title)

# ->In the print() function, you output multiple variables, separated by a comma:

a = "Python"
b = "is"
c = "awesome"
print(a,b,c)



#-> You can also use the + operator to output multiple variables:
# ->Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

a = "Python"
b = "is"
c = "awesome"
print(a+b+c)


# -> For numbers, the + character works as a mathematical operator:

a=10
b=5
print(a+b)



# ->In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

a=5
b="Your Name"
# print(a+b)
#TypeError: unsupported operand type(s) for +: 'int' and 'str'




#Global Variables

#-> A global variable in Python is a variable declared outside of any function or class scope, making it accessible throughout the entire code module

# -> Global variables can be used by everyone, both inside of functions and outside.

a = "Coder"

def myfunc():
  print("Hello :" + a)

myfunc()


#->If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.


a = "awesome"

def myfunc():
  a = "fantastic"
  print("Python is " + a)

myfunc()

print("Python is " + a)



#The global Keyword

#-> Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

#-> To create a global variable inside a function, you can use the global keyword.

def myfunc():
  global a
  a = "fantastic"

myfunc()

print("Python is " + a)

#-> Also, use the global keyword if you want to change a global variable inside a function.


a = "awesome"

def myfunc():
  global a
  a = "fantastic"

myfunc()

print("Python is " + a)