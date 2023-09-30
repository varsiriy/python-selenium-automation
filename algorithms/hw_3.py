 # Find the two lowest elements.

def find_two_lowest(arr: list):
    arr.sort()
    return [arr[0], arr[1]]
print(find_two_lowest([198, 3, 4, 9, 10, 2]))


 # Return the inverse of each.
 # Each positive becomes a negative, and the negatives become positives

def invert_list(arr: list):
    for i in range(len(arr)):
        arr[i] = -arr[i]
    return arr

print(invert_list([1, 5, -2, 4]))


 # Returns the difference between the largest and the smallest value in a given list.

def max_diff(arr: list):
    arr.sort()
    return arr[-1] - arr[0]

print(max_diff([3, 5, 7, 2]))


 # Count the number of elements in a given list larger than their adjacent neighbors

def count_larger_neighbor(arr: list):
    count = 0

    for i in range(1, len(arr) -1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            count += 1

    return count

print(count_larger_neighbor([2, 56, 7, 21, 22, 19, 26]))


 # Find the minimum element in the list and subtract it from each element in the array

def subtract_min(arr: list):
    min_e = min(arr)

    for i in range(len(arr)):
        arr[i] = arr[i] - min_e
    return arr

print(subtract_min([9, 2, 5, 4, 7, 6, 1]))


