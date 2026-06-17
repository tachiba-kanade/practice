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
Shell sort algorithm

Non Comparison-Based Sorting Algorithms

Counting sort algorithm
Bucket sort algorithm
Radix sort algorithm
Pigeonhole sort algorithm


| Algorithm      |       Best |    Average |      Worst |    Space | Stable?    |
| -------------- | ---------: | ---------: | ---------: | -------: | ---------- |
| Bubble Sort    |       O(n) |      O(n²) |      O(n²) |     O(1) | Yes        |
| Insertion Sort |       O(n) |      O(n²) |      O(n²) |     O(1) | Yes        |
| Selection Sort |      O(n²) |      O(n²) |      O(n²) |     O(1) | No         |
| Quick Sort     | O(n log n) | O(n log n) |      O(n²) | O(log n) | Usually no |
| Merge Sort     | O(n log n) | O(n log n) | O(n log n) |     O(n) | Yes        |
| Heap Sort      | O(n log n) | O(n log n) | O(n log n) |     O(1) | No         |
| Shell Sort     |    Depends |    Depends |    Depends |     O(1) | No         |
| Tim Sort       |       O(n) | O(n log n) | O(n log n) |     O(n) | Yes        |


"""

# 1. Bubble sorting - mostly the best number is swapped untill it goes till the end and iteration stops once no single swapping is done

def bubble_sort(bub_nums):
    n = len(bub_nums)
    swapped = False

    

bub_nums = [8, 3, 5, 1, 6]
print(bubble_sort(bub_nums))



# Classic Selection Sort (most common)
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

# MERGE SORT

def merge_sort(arr):
    # Base case: lists with 0 or 1 elements are already sorted
    if len(arr) <= 1:
        return arr
        
    # Divide: Find the midpoint and split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Conquer: Recursively sort both halves
    merge_sort(left_half)
    merge_sort(right_half)

    # Combine: Merge the sorted halves back into the original array
    i = j = k = 0

    # Copy data to temporary arrays left_half and right_half
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Checking if any element was left in left_half
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Checking if any element was left in right_half
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

# Example Usage:
if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", data)
    merge_sort(data)
    print("Sorted array:  ", data)

# INTERTION

def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        # Place the key at its correct position
        arr[j + 1] = key

# Example usage:
data = [12, 11, 13, 5, 6]
insertion_sort(data)
print("Sorted array:", data)
# Output: Sorted array: [5, 6, 11, 12, 13]
