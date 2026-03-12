import random
import time
import tracemalloc


# -------------------------
# Merge Sort Implementation
# -------------------------

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# -------------------------
# Quick Sort Implementation
# -------------------------

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# -------------------------
# Function to test algorithm
# -------------------------

def test_algorithm(name, algorithm, data):

    tracemalloc.start()

    start = time.perf_counter()
    algorithm(data.copy())
    end = time.perf_counter()

    memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    print(name)
    print("Execution Time:", round(end-start, 6), "seconds")
    print("Memory Usage:", memory, "bytes")
    print("---------------------------")


# -------------------------
# Generate datasets
# -------------------------

size = 1000

sorted_data = list(range(size))
reverse_sorted_data = list(range(size, 0, -1))
random_data = [random.randint(1, size) for _ in range(size)]


print("===== SORTED DATA =====")
test_algorithm("Merge Sort", merge_sort, sorted_data)
test_algorithm("Quick Sort", quick_sort, sorted_data)

print("\n===== REVERSE SORTED DATA =====")
test_algorithm("Merge Sort", merge_sort, reverse_sorted_data)
test_algorithm("Quick Sort", quick_sort, reverse_sorted_data)

print("\n===== RANDOM DATA =====")
test_algorithm("Merge Sort", merge_sort, random_data)
test_algorithm("Quick Sort", quick_sort, random_data)