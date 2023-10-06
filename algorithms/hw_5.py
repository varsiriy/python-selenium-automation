# Selection Sort. Descending

def selection_sort_descending(arr:list):
    for i in range(len(arr)):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr

test_data = [4, 5, 7, 2, 1, 3, 6]
print(test_data)
selection_sort_descending(test_data)
print(test_data)


# Bubble Sort. Descending

def bubble_sort_descending(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


test_data = [4, 5, 7, 2, 1, 3, 6]
print(test_data)
bubble_sort_descending(test_data)
print(test_data)


 # Insetion Sort. Descending

def insertion_sort_descending(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

test_data = [4, 5, 7, 2, 1, 3, 6]
print(test_data)
insertion_sort_descending(test_data)
print(test_data)