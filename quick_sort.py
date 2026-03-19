import random
import time

# -------------------------------
# Deterministic Quicksort
# -------------------------------
def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    
    return deterministic_quicksort(left) + [pivot] + deterministic_quicksort(right)


# -------------------------------
# Randomized Quicksort
# -------------------------------
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    
    remaining = arr[:pivot_index] + arr[pivot_index + 1:]
    left = [x for x in remaining if x <= pivot]
    right = [x for x in remaining if x > pivot]
    
    return randomized_quicksort(left) + [pivot] + randomized_quicksort(right)


# -------------------------------
# Testing Different Input Types
# -------------------------------
def test_quicksort():
    test_cases = {
        "Random Array": [8, 3, 1, 7, 0, 10, 2],
        "Sorted Array": [1, 2, 3, 4, 5, 6, 7],
        "Reverse Sorted Array": [7, 6, 5, 4, 3, 2, 1],
        "Repeated Values Array": [5, 3, 5, 2, 5, 1, 5]
    }

    for name, arr in test_cases.items():
        print(f"\n{name}")
        print("Original:", arr)
        print("Deterministic Quicksort:", deterministic_quicksort(arr))
        print("Randomized Quicksort:", randomized_quicksort(arr))


test_quicksort()
