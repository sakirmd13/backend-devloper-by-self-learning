#Write a Python program that takes two integer inputs from the user (rows and columns). Use a nested while loop to print the row and column numbers. Inside the inner loop, use if, elif, and else conditions such that when the column number is 1, use the continue statement; when the column number is 3, use the break statement; otherwise, use the pass statement and print the current row and column numbers. Add an else clause to both the inner and outer while loops, maintain counters using += to count the total iterations, and finally print the total number of outer loop iterations, inner loop iterations, and displayed values.Here's a Python program that 

# Program: Nested while loop with if, elif, else, continue, break, pass, and else clause

# User Input
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Counters
row = 1
outer_iterations = 0
inner_iterations = 0
displayed_values = 0

# Outer While Loop
while row <= rows:
    outer_iterations += 1
    print(f"\nRow {row}")

    col = 1

    # Inner While Loop
    while col <= cols:
        inner_iterations += 1

        if col == 1:
            col += 1
            continue

        elif col == 3:
            print(f"Break executed at Row = {row}, Column = {col}")
            break

        else:
            pass
            print(f"Row = {row}, Column = {col}")
            displayed_values += 1

        col += 1

    else:
        print(f"Inner while loop completed normally for Row {row}")

    row += 1

else:
    print("\nOuter while loop completed successfully.")

# Final Output
print("\n========== Summary ==========")
print("Total Outer Loop Iterations :", outer_iterations)
print("Total Inner Loop Iterations :", inner_iterations)
print("Total Displayed Values      :", displayed_values)

