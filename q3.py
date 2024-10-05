'''
Write a Python function print_multiplication_table(number, range_limit) that takes a number and a range limit as input, and prints the multiplication table for the given number up to the specified range.
'''

def print_multiplication_table(number, range_limit):
    for i in range(1, range_limit + 1):
        print(f"{number} x {i} = {number * i}")
        print()


print_multiplication_table(5, 10) 
