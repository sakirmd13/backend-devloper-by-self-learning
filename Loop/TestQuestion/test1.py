    
#Example 10: while loop with a if, else, elif ,for ,range (a,b,c) and break statement and continue statement and pass statement and nested loop with a nested loop and break statement and continue statement and pass statement and else clause and user input
count = 0
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
while count < num1:
    print(f"Outer loop count: {count}")
    inner_count = 0
    while inner_count < num2:
        print(f"  Inner loop count: {inner_count}")
        if inner_count == 2:
            print("  Breaking out of the inner loop.")
            break
        elif inner_count == 1:
            print("  Continuing to the next iteration of the inner loop.")
            inner_count += 1
            continue
        else:
            print("  This is a pass statement.")
            pass
        inner_count += 1
    else:
        print("  Inner loop completed without encountering a break statement.")
    count += 1
    
# if the user enters 2 and 5, the output will be:

# Enter the first number: 2
# Enter the second number: 5


#The output will be:
# Outer loop count: 0
#   Inner loop count: 0
#   This is a pass statement.

#   Inner loop count: 1
#   Continuing to the next iteration of the inner loop.

#   Inner loop count: 2
#   Breaking out of the inner loop.

# Outer loop count: 1
#   Inner loop count: 0
#   This is a pass statement.

#   Inner loop count: 1
#   Continuing to the next iteration of the inner loop.

#   Inner loop count: 2
#   Breaking out of the inner loop.


