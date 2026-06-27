#Python Data Types
# What are data types in python

# -> A data type in Python is a classification that defines the category of a value, determining how the computer stores it and what operations can be performed on it. 

# Since Python treats everything as an object, 

# data types are actually classes, and variables are instances of these classes. 

# Python is dynamically typed, meaning you do not need to explicitly declare a data type when creating a variable; the Python interpreter infers it automatically based on the value assigned


#Python has the following data types built-in by default, in these categories:

#    Text Type:	       str
#    Numeric Types:	   int, float, complex
#    Sequence Types:   list, tuple, range
#    Mapping Type:	   dict
#    Set Types:	       set, frozenset
#    Boolean Type:	   bool
#    Binary Types:	   bytes, bytearray, memoryview
#    None Type:	       NoneType


#Getting the Data Type

# -> You can get the data type of any object or variable in Python by using the built-in type() function.

# The type() FunctionPass the variable or value into type(), and wrap it in a print() statement to see the output

name="Your Name :"
print(type(name))


#Setting the Data Type

# -> In Python, you set a variable's data type automatically by assigning a value to it, or explicitly by using a constructor function (type casting). Because Python is a dynamically typed language, it automatically determines the data type based on the value you provide


# Implicit Setting (Implicit Assignment)

# -> You do not need to declare data types beforehand. Python sets the data type the moment you assign data to a variable


your_age=20     #int
print(type(your_age))


name="Your Name :"      #str
print(type(name))

product_price =9.0      #float
print(type(product_price))

table=1j    #complex
print(type(table))

you_subscribed_me=True      #bool
print(type(you_subscribed_me))

shoping_cart=["Laptop","Tablet"] #list
print(type(shoping_cart))



shoping_cart=("Laptop","Tablet") #tuple
print(type(shoping_cart))


shoping_cart={"Laptop","Tablet"} #set
print(type(shoping_cart))


shoping_cart={"product_name":"Laptop","Product_price":30000}        #dict
print(type(shoping_cart))

fruits= frozenset({"apple", "banana", "cherry"})    #frozenset
print(type(fruits))


steps = range(6)        #range
print(type(steps))


name=None       #noneType
print(type(name))


a= b"Hello"     #bytes
print(type(a))

a= bytearray(5)	#bytearray	
print(type(a))

x = memoryview(bytes(5))	#memoryview
print(type(x))