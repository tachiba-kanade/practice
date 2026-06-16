def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j]= nums[j+1]
                nums[j+1]=temp

nums = [3,4,7,6,9,10,5]
sort(nums)
print(nums)

"""Usually bubble sort runs in 0^2 but theres more efficient way to do so"""

# Optimized Python program for implementation of Bubble Sort
def bubbleSort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False


                # arr[0] and arr[1]
                # 64 and 34

                #  arr[1] and arr[2]
                #  64 and 25

                # arr[2] and arr[3]
                # 64 and 12

        # After each pass, one largest element is already sorted.
        # No need to check 64 again.
        #So second pass checks fewer elements.

        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

# Driver code to test above
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubbleSort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")