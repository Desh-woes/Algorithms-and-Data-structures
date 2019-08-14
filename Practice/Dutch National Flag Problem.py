def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # Sort the zero's first
    pointer1, pointer2 = 0, 0

    while pointer2 < len(input_list):
        if input_list[pointer1] == 0 and input_list[pointer2] == 0:
            pointer1 += 1
            pointer2 += 1
        elif input_list[pointer1] !=0 and input_list[pointer2] != 0:
            pointer2 += 1
        elif input_list[pointer1] != 0 and input_list[pointer2] == 0:
            input_list[pointer2] = input_list[pointer1]
            input_list[pointer1] = 0
            pointer1 += 1
            pointer2 += 1

    # Sort the two's next
    pointer1, pointer2 = len(input_list)-1, len(input_list)-1

    while pointer2 > 0:
        if input_list[pointer1] == 2 and input_list[pointer2] == 2:
            pointer1 -= 1
            pointer2 -= 1
        elif input_list[pointer1] != 2 and input_list[pointer2] != 2:
            pointer2 -= 1
        elif input_list[pointer1] != 2 and input_list[pointer2] == 2:
            input_list[pointer2] = input_list[pointer1]
            input_list[pointer1] = 2
            pointer1 -= 1
            pointer2 -= 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])