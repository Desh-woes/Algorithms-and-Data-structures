# Basic quick sort interface
def quick_sort(arr):
    quick_sort2(arr, 0, len(arr)-1)


# Recursive quick sort function
def quick_sort2(arr, first, last):
    # While this list does not contain only one element:
    if first < last:

        # Call the partition function which sorts both sides of the pivot
        p = partition(arr, first, last)

        # Call the quick sort function on the other halves of the array recursively
        quick_sort2(arr, first, p-1)
        quick_sort2(arr, p+1, last)


# Function to generate our pivot index using the median of three values approach
def get_pivot(arr, first, last):
    middle = (first+last)//2
    pivot = last
    if arr[last] < arr[middle]:
        if arr[middle] < arr[last]:
            pivot = middle
    elif arr[last] < arr[first]:
        pivot = last

    return pivot


# Partition function to sort our pivot value
def partition(arr, first, last):
    pivot_index = get_pivot(arr, first, last)
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[first] = arr[first], arr[pivot_index]
    border = first

    for i in range(first, last+1):
        if arr[i] < pivot_value:
            border += 1
            arr[i], arr[border] = arr[border], arr[i]
    arr[first], arr[border] = arr[border], arr[first]

    return border


# Test parameters
arr_test = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
quick_sort(arr_test)
print(arr_test)


