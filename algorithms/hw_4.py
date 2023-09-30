 # Sum and multiplication of even and odd numbers. The sum of all even numbers. The product of all odd numbers.

def sum_even_and_product_odd(arr: list):
    sum_even = 0
    product_odd = 1

    for number in arr:
        if number % 2 == 0:
            sum_even += number
        else:
            product_odd *= number

    return [sum_even, product_odd]

test_data = [1, 2, 3, 4]
print(sum_even_and_product_odd(test_data))


 # Sum between range values. Within the range [min, max], inclusive.

def sum_between_range(arr: list, min_val: int, max_val: int):
    result = 0
    for number in arr:
        if number >= min_val and number <= max_val:
            result += number

    return result


test_arr = [3, 2, 1, 4, 10, 8, 7, 6, 9, 5]
min_val = 3
max_val = 7
print(sum_between_range(test_arr, min_val, max_val))


 # Increment a Number. nonnegative decimal integer D and updates the list to represent the integer D + 1.
 # For example, if the input is [1, 2, 9] then you should update the list to [1, 3, 0].

def plus_one(arr: list):
    arr[-1] += 1

    for i in reversed(range(1, len(arr))):
        if arr[i] !=10:
            break
        else:
            arr[i] = 0
            arr[i - 1] += 1

    if arr[0] == 10:   # [9, 9, 9] -> [1, 0, 0, 0]
        arr[0] = 1
        arr.append(0)

    return arr

test_data = [1, 2, 9]
print(plus_one(test_data))


