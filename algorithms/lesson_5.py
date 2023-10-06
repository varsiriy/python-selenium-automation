 # Nested loop sort

adj = ["red", "ripe", "tasty"]
fruits = ["apple", "banana", "cherry"]

for i in adj:
    for j in fruits:
        print(i + " " + j)


 # Selection Sort

def selection_sort(arr:list):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

test_data = [4, 2, 1, 7, 5, 3]
print(test_data)
print(selection_sort(test_data))


 # Bubble Sort

def bubble_sort(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

test_data = [4, 6, 2, 1, 5]
print(test_data)
bubble_sort(test_data)
print(test_data)


 # Insertion Sort

def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


test_data = [5, 3, 2, 1, 6, 4]
print(test_data)
insertion_sort(test_data)
print(test_data)

