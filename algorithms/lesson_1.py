 ### Swap two variables

  # built in function a, b = b, a

def swap_variables(a: int, b:int):
    print(f'a= {a}, b= {b}')
    a, b = b, a
    print(f'a= {a}, b= {b}')

test_a = 5
test_b = 10
swap_variables(test_a, test_b)

   # or

def swap_variable(a: int, b: int):
    print(f'a= {a}, b= {b}')
    temp = a
    a = b
    b = temp
    print(f'a= {a}, b= {b}')

test_a = 5
test_b = 10
swap_variable(test_a, test_b)

   # or

def swap_variable(a: int, b: int):
    print(f'a= {a}, b= {b}')
    a = a + b
    b = a - b
    a = a - b
    print(f'a= {a}, b= {b}')

test_a = 5
test_b = 10
swap_variable(test_a, test_b)


 ### FizzBuzz

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

fizzbuzz()

  # or

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

fizzbuzz(100)


 ### Factorial

def factorial(n: int):
    result = 1
    for i in range(2, n + 1):
        result = result * i
    print(f'The factorial of {n} is {result}')


factorial(1)


 ### Sum of three

def sum_of_three_digit_number(number:int):
    result = 0
    for i in range(3):
        current_number = number % 10
        result = result + current_number
        number = number // 10
    return result


test_result = sum_of_three_digit_number(291)  #12
print(test_result)
