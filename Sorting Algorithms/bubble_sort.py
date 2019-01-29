# Function to carry out our sorting operation
def sort_array(arr):

    # By default, our array is NOT sorted.
    array_sorted = False

    # While array is not sorted, go through the array and bubble the largest element to the end.
    while not array_sorted:

        # First set the array to be sorted.
        array_sorted = True

        # List end
        list_end = len(arr) - 1

        # Go through the array and check if there is any element that is out of place.
        for x in range(0, list_end):

            # If array value in position x is grater than array value in position x+1, swap.
            if arr[x] > arr[x+1]:
                swap(arr, x, x+1)

                # If we find any elements that are not sorted, then our array_sorted value becomes false
                array_sorted = False

        # Decrease our list end because we know the right part of our list is already sorted.
        list_end -= 1

    # If all elements have been sorted, the while loop ends and returns our sorted array.
    return arr


# Function to help with swapping elements
def swap(arr, position_1, position_2):
    temp = arr[position_1]
    arr[position_1] = arr[position_2]
    arr[position_2] = temp


# Test parameters
arr_test = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(sort_array(arr_test))