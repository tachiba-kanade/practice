"""
Bubble Sort → understand swapping.
Selection Sort → understand finding minimum.
Insertion Sort → understand shifting.
Merge Sort → understand divide and conquer.
Python's built-in sort() → what you'll actually use in projects.

"""

"""
Comparison-Based Sorting Algorithms

Bubble sort algorithm
Insertion sort algorithm
Selection sort algorithm
Quick sort algorithm
Heap sort algorithm
Merge sort algorithm

Non Comparison-Based Sorting Algorithms
Counting sort algorithm
Bucket sort algorithm
Radix sort algorithm

"""
# 1. Classic Selection Sort (most common)
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


nums = [8, 3, 5, 1, 6]
print(selection_sort(nums))
