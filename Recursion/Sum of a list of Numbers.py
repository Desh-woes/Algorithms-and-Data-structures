# Approach 1 -- Implementing the sum of numbers in a list without recursion.
# This approach makes use of an accumulator that starts at 0 and increases or decreases based on the sign of the number
# added to it
def list_sum1(arr):
    accumulator = 0
    for i in arr:
        accumulator += i

    return accumulator


# Approach 2 -- Implementing the sum of numbers in a list using a recursive algorithm.
def list_sum2(arr):
    # If there is only one item left in the list, return that single item
    if len(arr) == 1:
        return arr[0]

    # If there's more than one item in the list, return the sum of the first item to the rest of the items in the list.
    else:
        return arr[0] + list_sum2(arr[1:])


# Test Parameters.
test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_sum1(test_arr))
print(list_sum2(test_arr))
