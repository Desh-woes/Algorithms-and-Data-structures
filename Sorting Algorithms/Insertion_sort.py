# Function to help us with sorting our array
def sort_array(arr):
    # Insertion sort assumes that the elements to the left has been sorted
    for i in range(1, len(arr)):

        # Assign our current value to a variable
        current_value = arr[i]

        # Second iterator to check elements before (To the left of) our current value
        j = i - 1

        # Shift values to the right while our current value is less than the values to the left
        while j >= 0 and arr[j] > current_value:
            # Shift values
            arr[j+1] = arr[j]
            # Reduce our value of J to check the elements to the left of current value
            j -= 1

        # In a case where our current value is not less than the value in position J, insert current value into position
        # J+1
        arr[j + 1] = current_value

    # Return sorted array
    return arr


# Test parameters
arr_test = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(sort_array(arr_test))