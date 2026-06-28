

# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b


#Python If Statement
#The if statement in Python is used to make decisions. It executes a block of code only if a condition is True. If the condition is false, the code block is skipped

num1=10
num2=5
if num1<num2:
    print("less Than")
    
if num1 >num2:
    print("Greterthan")
    
    
# Indentation
# -> Indentation in Python means adding spaces (or a tab) at the beginning of a line to define a block of code. Unlike many other programming languages, Python uses indentation instead of {} (curly braces).

# Why is indentation important?

# It tells Python which statements belong together

# If statement, without indentation (will raise an error):

# num1=10
# num2=5
# if num1 >num2:
# print("Greterthan")
    
#Use 4 spaces for each indentation level (this is the Python standard)


# Multiple Statements in If Block
# You can have multiple statements inside an if block. All statements must be indented at the same level.

age = 18

if age >= 18:
    print("You are an adult.")
    print("You can vote.")

print("Program finished.")


# Using Variables in Conditions
# Boolean variables can be used directly in if statements without comparison operators.
is_logged_in = True
if is_logged_in:
  print("Welcome back!")
  
  
  
# Nested If Statements
# You can have if statements inside if statements. This is called nested if statements.

age = 50

if age >= 16:
    print("You are an adult.")
    if age>=18:
        print("You Can vote")
        
#A nested if is an if statement placed inside another if statement. The inner if is checked only if the outer if condition is True.


#How Nested If Works
# Each level of nesting creates a deeper level of decision-making. The code evaluates from the outermost condition inward.
#A nested if is an if statement placed inside another if statement. The inner if is checked only if the outer if condition is True.


# Multiple Levels of Nesting
# You can nest as many levels deep as needed, but keep in mind that too many levels can make code harder to read.

score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
      
# Nested If vs Logical Operators
# Sometimes nested if statements can be simplified using logical operators like and. The choice depends on your logic.

temperature = 25
is_sunny = True

if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!")


if temperature > 20 and is_sunny:
  print("Perfect beach weather!")
  
#Both approaches produce the same result. Use nested if statements when the inner logic is complex or depends on the outer condition. Use and when both conditions are simple and equally important.


#Else Statement
#The else statement is used with an if statement. It executes a block of code when the if condition is False.
age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
    
    
#Positive or Negative Number
number = -5

if number >= 0:
    print("Positive number")
else:
    print("Negative number")
    
#Even or Odd Number
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
    

#Else as Fallback
# The else statement acts as a fallback that executes when none of the preceding conditions are true. This makes it useful for error handling, validation, and providing default values.
password = "python123"
if password == "python123":
    print("Login successful")
else:
    print("Incorrect password")
    
    
    
#Elif Statement
#The elif statement (short for "else if") is used to check multiple conditions. It comes after an if statement and before an else statement.

# When to Use Elif
# Use elif when you have multiple mutually exclusive conditions to check. This is more efficient than using multiple separate if statements because Python stops checking once it finds a true condition.
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
    
    
#Day of the Week
day = 6

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day")
    
    
#temperature
temperature = 32

if temperature >= 40:
    print("Very Hot")
elif temperature >= 30:
    print("Hot")
elif temperature >= 20:
    print("Warm")
elif temperature >= 10:
    print("Cool")
else:
    print("Cold")
    
    
#Shorthand If
#If you have only one statement to execute, you can put it on the same line as the if statement.
a= 5
b = 2
if a > b : print("a is greater than b")

#Note: You still need the colon : after the condition.


#Short Hand If ... Else
# If you have one statement for if and one for else, you can put them on the same line using a conditional expression:
a = 2
b = 330
print("A") if a > b else print("B")
# This is called a conditional expression (sometimes known as a "ternary operator").


# Assign a Value With If ... Else
# You can also use a one-line if/else to choose a value and assign it to a variable:
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)


# Multiple Conditions on One Line
# You can chain conditional expressions, but keep it short so it stays readable:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")



# When to Use Shorthand If
# Shorthand if statements and ternary operators should be used when:

# The condition and actions are simple
# It improves code readability
# You want to make a quick assignment based on a condition

# Important: While shorthand if statements can make code more concise, avoid overusing them for complex conditions. For readability, use regular if-else statements when dealing with multiple lines of code or complex logic.



# Comparison Operators:
# Comparison operators are used to compare two values. They return a Boolean value:

# True if the comparison is correct.
# False if the comparison is incorrect


x = 10
y = 20

print(x == y)   # False — equal to
print(x != y)   # True  — not equal
print(x > y)    # False — greater than
print(x < y)    # True  — less than
print(x >= y)   # False — greater or equal
print(x <= y)   # True  — less or equal



# Logical Operators
# Logical operators are used to combine two or more conditions. They return either True or False.
# Logical operators are used to combine conditional statements. Python has three logical operators:

# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Reverses the result, returns False if the result is true

# The and Operator
# The and keyword is a logical operator, and is used to combine conditional statements. Both conditions must be true for the entire expression to be true.
#The and operator returns True only when both conditions are True.


# and Operator Truth Table
# Condition 1	Condition 2	    Result
# True  	    True	        True
# True  	    False	        False
# False     	True	        False
# False	        False	        False
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
    
    
# The or Operator
# The or keyword is a logical operator, and is used to combine conditional statements. At least one condition must be true for the entire expression to be true.

# The or operator returns True if at least one condition is True.

# or Operator Truth Table
# Condition 1	Condition 2	Result
# True	        True	    True
# True	        False	    True
# False	        True	    True
# False	        False	    False
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
    
# The not Operator
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement.
# The not operator reverses the Boolean result.

# or Operator Truth Table
# Condition 1		Result
# True	        	False
# False	       	    True
        	    

is_logged_in = False

if not is_logged_in:
    print("Please log in.")


# Pass Statement
# The pass statement is a placeholder in Python. It does nothing when executed.
# It is useful when Python requires a statement, but you don't want to write any code yet.
# During development, you might want to sketch out your program structure before implementing the details. The pass statement allows you to do this without syntax errors.
age = 18

if age >= 18:
    pass

print("Program continues")
# The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.


# Why Use pass?
# The pass statement is useful in several situations:

# When you're creating code structure but haven't implemented the logic yet
# When a statement is required syntactically but no action is needed
# As a placeholder for future code during development
# In empty functions or classes that you plan to implement later


# pass vs Comments
# A comment is ignored by Python, but pass is an actual statement that gets executed (though it does nothing). You need pass where Python expects a statement, not just a comment.
score = 85

if score > 90:
  pass# This is excellent
# This will raise an IndentationError



# This will cause an error (empty code block):

# score = 85

# if score > 90:
#   # This is excellent
# # This will raise an IndentationError


# pass with Multiple Conditions
# You can use pass in any branch of an if-elif-else statement.

value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")
  
  
  
# pass in Other Contexts
# While we focus on pass with if statements here, it's also commonly used with loops, functions, and classes.


# Using pass with functions:

def calculate_discount(price):
  pass # TODO: Implement discount logic

# Function exists but doesn't do anything yet