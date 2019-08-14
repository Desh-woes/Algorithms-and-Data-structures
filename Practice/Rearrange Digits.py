def merge_sort(arr):
    return _merge_sort_helper(arr)


def _merge_sort_helper(arr):
    if len(arr) <= 1:
        return arr

    mid_index = len(arr) // 2
    left_arr = arr[:mid_index]
    right_arr = arr[mid_index:]

    left_part = _merge_sort_helper(left_arr)
    right_part = _merge_sort_helper(right_arr)

    return merge_arr(left_part, right_part)


def merge_arr(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    input_list = merge_sort(input_list)

    digit1 = ""
    digit2 = ""

    for i in range(len(input_list)):
        if i % 2 == 0:
            digit1 = str(input_list[i]) + digit1
        else:
            digit2 = str(input_list[i]) + digit2

    return int(digit1), int(digit2)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]