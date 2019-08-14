def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    return _helper_func(0, number, number)


def _helper_func(start_value, end_value, target):
    # Get the mid point
    mid_point = (start_value + end_value)//2

    # Condition if the square of our mid point is less than out target
    if mid_point**2 < target:
        # If the square of the next largest value is greater than our target, the return out current value.
        if (mid_point+1)**2 > target:
            return mid_point
        # Else, find the next best target
        return _helper_func(mid_point+1, end_value, target)

    # Find a lower middle point
    elif mid_point**2 > target:
        return _helper_func(start_value, mid_point-1, target)

    # Else if we have found the best target, return it.
    else:
        return mid_point


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
