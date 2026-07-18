# Assignment 4
# Part 1: Heapsort
# Bilal Khalid

import random
import time

# Heap Sort Functions

def heapify(arr, n, i):
    # This function keeps the heap property valid.

    # Assume current node is the largest
    largest = i

    # Left child
    left = 2 * i + 1

    # Right child
    right = 2 * i + 2

    # Check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not current node,
    # swap the values
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Continue heapifying
        heapify(arr, n, largest)

def heap_sort(arr):
    # Main Heap Sort function.

    n = len(arr)

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Remove one element at a time
    for i in range(n - 1, 0, -1):

        # Move current largest element
        # to the end
        arr[i], arr[0] = arr[0], arr[i]

        # Restore heap
        heapify(arr, i, 0)

# Quick Sort

def quick_sort(arr):
    # Simple Quick Sort implementation.

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = []
    middle = []
    right = []

    for value in arr:

        if value < pivot:
            left.append(value)

        elif value == pivot:
            middle.append(value)

        else:
            right.append(value)

    return quick_sort(left) + middle + quick_sort(right)

# Merge Sort

def merge_sort(arr):
    # Simple Merge Sort implementation.

    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)


def merge(left, right):
    # Merge two sorted lists.

    result = []

    i = 0
    j = 0

    # Compare values from both lists
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    # Add remaining values
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Helper Functions

def create_random_list(size):
    # Create a list with random numbers.

    numbers = []

    for _ in range(size):
        numbers.append(random.randint(1, 100000))

    return numbers

def create_sorted_list(size):
    # Create an already sorted list.

    return list(range(size))


def create_reverse_list(size):
    # Create a reverse sorted list.

    return list(range(size, 0, -1))

# Timing Function

def measure_time(sort_name, data):
    # Measure execution time of a sorting algorithm.

    copied = data.copy()

    start = time.perf_counter()

    if sort_name == "Heap":
        heap_sort(copied)

    elif sort_name == "Quick":
        quick_sort(copied)

    elif sort_name == "Merge":
        merge_sort(copied)

    end = time.perf_counter()

    return end - start

# Main Program

print("----------------------------------------")
print("Heap Sort Performance Comparison")
print("----------------------------------------")

sizes = [1000, 5000, 10000]

for size in sizes:

    print("\nInput Size:", size)

    datasets = {
        "Random": create_random_list(size),
        "Sorted": create_sorted_list(size),
        "Reverse": create_reverse_list(size)
    }

    for name, data in datasets.items():

        print("\nData Type:", name)

        heap_time = measure_time("Heap", data)
        quick_time = measure_time("Quick", data)
        merge_time = measure_time("Merge", data)

        print("Heap Sort : {:.6f} seconds".format(heap_time))
        print("Quick Sort: {:.6f} seconds".format(quick_time))
        print("Merge Sort: {:.6f} seconds".format(merge_time))
