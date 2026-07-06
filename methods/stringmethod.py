
#String Methods
# Python strings have many built-in methods. Here are some of the most commonly used

# | Method               | Description                                  | Example                                   |
# | -------------------- | -------------------------------------------- | ----------------------------------------- |
# | `lower()`            | Converts to lowercase                        | `"HELLO".lower()` → `'hello'`             |
# | `upper()`            | Converts to uppercase                        | `"hello".upper()` → `'HELLO'`             |
# | `capitalize()`       | Capitalizes first letter                     | `"python".capitalize()` → `'Python'`      |
# | `title()`            | Capitalizes each word                        | `"hello world".title()` → `'Hello World'` |
# | `strip()`            | Removes spaces from both ends                | `" hi ".strip()` → `'hi'`                 |
# | `lstrip()`           | Removes left spaces                          | `" hi".lstrip()` → `'hi'`                 |
# | `rstrip()`           | Removes right spaces                         | `"hi ".rstrip()` → `'hi'`                 |
# | `replace(old, new)`  | Replaces substring                           | `"cat".replace("c","b")` → `'bat'`        |
# | `find(sub)`          | Returns index of substring                   | `"hello".find("e")` → `1`                 |
# | `index(sub)`         | Like `find()`, but raises error if not found | `"hello".index("e")` → `1`                |
# | `count(sub)`         | Counts occurrences                           | `"banana".count("a")` → `3`               |
# | `split(sep)`         | Splits string into list                      | `"a,b,c".split(",")` → `['a','b','c']`    |
# | `join(iterable)`     | Joins iterable into string                   | `"-".join(['a','b'])` → `'a-b'`           |
# | `startswith(prefix)` | Checks prefix                                | `"python".startswith("py")` → `True`      |
# | `endswith(suffix)`   | Checks suffix                                | `"python".endswith("on")` → `True`        |
# | `isalpha()`          | All letters?                                 | `"abc".isalpha()` → `True`                |
# | `isdigit()`          | All digits?                                  | `"123".isdigit()` → `True`                |
# | `isalnum()`          | Letters and digits only?                     | `"abc123".isalnum()` → `True`             |
# | `isspace()`          | All whitespace?                              | `"   ".isspace()` → `True`                |


s = "  Hello, Python!  "

print(s.strip())          # Hello, Python!
print(s.lower())          # hello, python!
print(s.upper())          # HELLO, PYTHON!
print(s.replace("Python", "World"))  # Hello, World!
print(s.split(","))       # ['  Hello', ' Python!  ']




name = "  Hello Python World  "

print(name.upper())          # HELLO PYTHON WORLD
print(name.lower())          # hello python world
print(name.strip())          # remove spaces
print(name.replace("Python", "Backend"))
print(name.split())          # ['Hello', 'Python', 'World']
print("hello".capitalize())  # Hello
print("hello world".title()) # Hello World
print(name.count("o"))       # count 'o'
print(name.find("Python"))   # find index
print("  ".isspace())        # True
print("hello123".isalnum())  # True
print("hello".startswith("he"))  # True
print("hello".endswith("lo"))    # True


#dir() is a built-in Python function that lists the attributes and methods of an object.
# Syntax
# dir(object)
# If you pass an object, it returns a list of its methods and attributes.
# If you call dir() with no arguments, it lists the names in the current scope.

# Example 1: dir() with a string
s = "Python"

print(dir(s))

# Output (partial):

# ['__add__', '__class__', '__contains__', ..., 'capitalize',
#  'count', 'endswith', 'find', 'index', 'join', 'lower',
#  'replace', 'split', 'strip', 'upper', ...]

# This shows all the methods available for string objects.

# Example 2: dir() with a list
numbers = [1, 2, 3]

print(dir(numbers))


# Example 3: dir() with no arguments
x = 10
name = "Alice"

print(dir())

# Output:

# ['__annotations__', '__builtins__', '__doc__', '__name__', 'name', 'x']

# This lists the variables and names currently defined in your program.

# Why use dir()?
# To discover what methods an object has.
# To explore unfamiliar objects or libraries.
# To learn Python interactively in the Python shell or Jupyter Notebook.

# For example, if you're not sure what you can do with a string:

s = "hello"
print(dir(s))