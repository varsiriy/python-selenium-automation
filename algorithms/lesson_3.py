lst_words = ["apple", "kiwi", "banana", "orange"]
lst_numbers = [3, 4, 2, 1, 2, 5]

lst_words.append("coconut")  # add element to the list
print(lst_words)

lst_words.clear()  # remove elements from the list
print(lst_words)

print(lst_numbers.count(2))  # count the occurrences of a specific element in the list

print(lst_numbers.index(2))  # to find the index of the first occurrence of an element in the list[0, 1, 2]

lst_numbers.insert(3, 99)  # add an element at a specific index
print(lst_numbers)

lst_numbers.pop(1)  # to remove an element form a specific index (-1 by default)
print(lst_numbers)

lst_numbers.remove(4)  # to remove the firs occurrence of a specific element
print(lst_numbers)

lst_numbers.reverse()  # reverse the order of elements in the list
print(lst_numbers)

lst_numbers.sort()  # sort the list in ascending order
print(lst_numbers)


 # Find the Missing Element

def find_missing_element(arr1: list, arr2: list):
    arr1.sort()
    arr2.sort()
    print(arr1)
    print(arr2)

    for i in range(len(arr2) -1):
        if arr1[i] != arr2[i]:
            print(str(arr1[i]) + " is the missing element")
            return
    print(str(arr1[-1]) + "is the missing element")

testlist1 = [1, 3, 2, 4, 5, 7, 9]
testlist2 = [3, 2, 1, 5, 9, 7]
find_missing_element(testlist1, testlist2)


 # Given an array of integers (positive and negative) find the largest continuous sum

def largest_count_sum(arr:list):
    cur_sum = max_sum = arr[0]

    for num in arr[1:]:
        cur_sum = max(cur_sum + num, num)
        max_sum = max(max_sum, cur_sum)

    return max_sum


test_list = [-4, 2, -1, 3, 4, 10, 10, -10, -1]
print(largest_count_sum(test_list))


 # Mountain array

def mountain_array(arr: list):
    i = 1
    while i < len(arr) and arr[i - 1] < arr[i]:
        i += 1

    if i == 1 or i == len(arr):
        return False

    while i <len(arr) and arr[i - 1] > arr[i]:
        i += 1

    if i == len(arr):
        return True
    else:
        return False


test_array = [1, 3, 4, 7, 5, 3]
print(mountain_array(test_array))