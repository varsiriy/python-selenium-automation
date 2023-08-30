#  1. There is a program that prints the numbers from 1 to 100.
# If the number is divisible of 3, print “Bin”
# If the number is divisible of 7, print “Go”
# For numbers which are divisible of 3 and 7, print “BinGo”

# def foo_bar(n: int):
#     for i in range(1, 101):
#         if i % 3 == 0 and i % 7 == 0:
#             print('BinGo')
#         elif i % 3 == 0:
#             print('Bin')
#         elif i % 7 == 0:
#             print('Go')
#         else:
#             print(i)
#
# foo_bar(100)


# 2. Compute the sum of digits in all numbers from 1 to n. When a function gets a number n,
# find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

# def sum_numbers(n: int):
#     final_sum = 0
#     for i in range(n + 1):
#         final_sum = final_sum + i
#     print(f'The sum of {n} is {final_sum}')
#
# sum_numbers(5)


# Find the max number from 3 values.
# Example: 124, 21, 32. Result = 124.

# def find_max(a: int, b: int, c: int):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c
#
# print(find_max(124, 21, 32))


#  Leap year.
# A leap year is exactly divisible by 4
# If it’s a century year (divisible by 100), it is a leap year if it’s also divisible by 400.
# If it’s divisible by 100 and not divisible by 400, it’s not a leap year.
#
# In other words, three conditions are used to identify leap years:
# The year can be evenly divided by 4, and is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year


# def leap_year(year: int):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print(f'{year} is a leap year')
#             else:
#                 print(f'{year} is not a leap year')
#         else:
#             print(f'{year} is a leap_year')
#     else:
#         print(f'{year} is not a leap year')
#
#
# leap_year(1992)
# leap_year(2000)
# leap_year(2100)
# leap_year(2071)


# Fibonacci.Print out the Fibonacci sequence until the given n-th in the sequence.


def generate_fibonacci_sequence(n: int):
    #Initialize the list with the first two Fibonacci numbers

    fib_sequence = [0, 1]

    # Use a for loop to generate the remaining Fibonacci numbers after the first two

    for i in range(2, n):
        new_number = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(new_number)

    # Calculate the next Fibonacci number using the formula fib_sequence[-1] + fib_sequence[-2]


    # Append the new Fibonacci number to the list using the append() function

    return fib_sequence

print(generate_fibonacci_sequence(10))
