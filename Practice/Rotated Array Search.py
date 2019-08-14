def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return _helper_func(input_list, 0, len(input_list)-1, number)


def _helper_func(arr, start_index, end_index, target):
    if start_index > end_index:
        return -1

    mid_index = (start_index+end_index)//2

    if arr[mid_index] == target:
        return mid_index

    # Obtain the sorted part
    if arr[mid_index] < arr[end_index]:
        if arr[mid_index] < target <= arr[end_index]:
            if arr[end_index] == target:
                return end_index
            return binary_search(arr, mid_index+1, end_index, target)
        return _helper_func(arr, start_index, mid_index-1, target)
    else:
        if arr[start_index] <= target < arr[mid_index]:
            if arr[start_index] == target:
                return start_index
            return binary_search(arr, start_index, mid_index-1, target)
        return _helper_func(arr, mid_index+1, end_index, target)


def binary_search(arr, start_index, end_index, target_value):
    if end_index < start_index:
        return -1
    # Get middle point
    mid_point = (start_index+end_index)//2

    if arr[mid_point] == target_value:
        return mid_point
    if arr[mid_point] > target_value:
        return binary_search(arr, start_index, mid_point-1, target_value)
    else:
        return binary_search(arr, mid_point+1, end_index, target_value)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# Test cases
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])