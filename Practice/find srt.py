def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    return _helper_func(number, 0, number)


def _helper_func(number, start_value, end_value):
    if end_value - start_value == 1:
        if end_value * end_value <= number:
            return end_value
        return start_value

    mid_value = (start_value + end_value) // 2

    if mid_value * mid_value <= number:
        if (mid_value + 1) * (mid_value + 1) > number:
            return mid_value
        return _helper_func(number, mid_value, end_value)

    else:
        return _helper_func(number, start_value, mid_value - 1)


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
