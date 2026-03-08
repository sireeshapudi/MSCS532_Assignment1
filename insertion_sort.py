# MSCS532 Assignment 1
# Insertion Sort in Monotonically Decreasing Order

def insertion_sort_desc(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1

        # move smaller elements to the right
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i -= 1

        arr[i + 1] = key

    return arr


numbers = [7, 9, 4, 6, 5, 8]

print("Original array:", numbers)

sorted_numbers = insertion_sort_desc(numbers)

print("Sorted array in decreasing order:", sorted_numbers)