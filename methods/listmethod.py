#In Python, list methods are built-in functions that let you modify and work with lists. Here are the most commonly used ones:

# | Method             | Description                                                  | Example                |
# | ------------------ | ------------------------------------------------------------ | ---------------------- |
# | `append(x)`        | Adds an item to the end of the list.                         | `lst.append(5)`        |
# | `extend(iterable)` | Adds all elements of an iterable to the list.                | `lst.extend([4, 5])`   |
# | `insert(i, x)`     | Inserts an item at a specified position.                     | `lst.insert(1, 10)`    |
# | `remove(x)`        | Removes the first occurrence of a value.                     | `lst.remove(3)`        |
# | `pop([i])`         | Removes and returns the item at index `i` (last by default). | `lst.pop()`            |
# | `clear()`          | Removes all items from the list.                             | `lst.clear()`          |
# | `index(x)`         | Returns the index of the first occurrence of a value.        | `lst.index(5)`         |
# | `count(x)`         | Returns the number of occurrences of a value.                | `lst.count(2)`         |
# | `sort()`           | Sorts the list in ascending order.                           | `lst.sort()`           |
# | `reverse()`        | Reverses the order of the list.                              | `lst.reverse()`        |
# | `copy()`           | Returns a shallow copy of the list.                          | `new_lst = lst.copy()` |


numbers = [3, 1, 4]

numbers.append(5)
print(numbers)      # [3, 1, 4, 5]

numbers.insert(1, 2)
print(numbers)      # [3, 2, 1, 4, 5]

numbers.remove(4)
print(numbers)      # [3, 2, 1, 5]

numbers.sort()
print(numbers)      # [1, 2, 3, 5]

numbers.reverse()
print(numbers)      # [5, 3, 2, 1]

print(numbers.count(2))   # 1

print(numbers.index(3))   # 1

last = numbers.pop()
print(last)         # 1
print(numbers)      # [5, 3, 2]

copy_list = numbers.copy()
print(copy_list)    # [5, 3, 2]

numbers.clear()
print(numbers)      # []




fruits = ["banana", "apple", "mango", "cherry"]

fruits.append("grape")     # add at end
fruits.insert(1, "kiwi")   # add at position
fruits.remove("apple")     # remove by value
fruits.pop()               # remove last item
fruits.sort()              # sort alphabetically
fruits.reverse()           # reverse the list
print(len(fruits))         # length
print(fruits.count("mango")) # count occurrences
print(fruits.index("mango")) # find index
fruits.clear()             # empty the list