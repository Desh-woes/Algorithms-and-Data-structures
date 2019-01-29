# Function to help with sorting our array
def sort_array(arr):

    # Outer loop to go through every element in position i
    for i in range(0, len(arr)-1):

        # Minimum value starts at position i
        min_value = i

        # Inner loop to compare elements in position I to every other element after it
        for j in range(i+1, len(arr)):

            # If current value(J) is less than the current minimum value, update the minimum value.
            if arr[j] < arr[min_value]:
                min_value = j

        # If the current minimum value is not equal to the value of i, swap the values
        if min_value != i:
            swap(arr, i, min_value)

    # Return the sorted array
    return arr


# Function to help with swapping elements
def swap(arr, position_1, position_2):
    temp = arr[position_1]
    arr[position_1] = arr[position_2]
    arr[position_2] = temp


# Test parameters
arr_test = [140, 89, 678, 767, 766, 765, 6764, 73, 562, 3451, 250, 2607]
print(sort_array(arr_test))