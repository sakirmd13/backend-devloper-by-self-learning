#Python While Loops

#A while loop in Python repeatedly executes a block of code as long as a specified condition is true.

#Example 1: Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1 # Increment the counter with each iteration to avoid an infinite loop.

#Example 2: while loop with user input
# user_input = ""
# while user_input != "quit":
#     user_input = input("Enter 'quit' to exit: ")
#     print(f"You entered: {user_input}")

#Example 3: while loop with a flag
# active = True
# while active:
#     user_input = input("Enter 'stop' to stop: ")
#     if user_input == "stop":
#         active = False
#     else:
#         print(f"You entered: {user_input}")

#Example 4: while loop with break statement
count = 0
while True:
    print(f"count: {count}")
    count += 1
    if count >= 5:
        break

#Example 5: while loop with continue statement
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(f"count of odd numbers: {count}")

#Example 6: while loop with else clause
count = 0
while count < 5:
    print(f"count: {count}")
    count += 1
else:
    print("Loop completed without encountering a break statement.")

#Example 7: while loop with else clause and break statement
count = 0
while count < 5:
    print(f"count: {count}")
    count += 1
    if count == 3:
        break
else:
    print("Loop completed without encountering a break statement.")
    
    
#Example 8: while loop with a nested loop
count = 0
while count < 3:
    print(f"Outer loop count: {count}")
    inner_count = 0
    while inner_count < 4:
        print(f"  Inner loop count: {inner_count}")
        inner_count += 1
    count += 1
    
    
#Example 9: while loop with a nested loop and break statement
count = 0
while count < 3:
    print(f"Outer loop count: {count}")
    inner_count = 0
    while inner_count < 4:
        print(f"  Inner loop count: {inner_count}")
        if inner_count == 2:
            print("  Breaking out of the inner loop.")
            break
        inner_count += 1
    count += 1
    
