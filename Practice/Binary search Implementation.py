# Sample list to work on
list_sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

# Set minimum and maximum values
min_value = 0
max_value = len(list_sample) - 1

# Set middle value guess// Value must be an integer
middle_point = (min_value + max_value) // 2

# Define target value
target = 17

# check if the value at the middle point is greater, less or equal to the target
while list_sample[middle_point] != target:

    # If middle point is less than target, adjust minimum value
    if list_sample[middle_point] < target:
        min_value = middle_point + 1

    # If middle point is grater than target, adjust maximum value
    elif list_sample[middle_point] > target:
        max_value = middle_point - 1

    # Change final middle point
    middle_point = (min_value + max_value) // 2


print(middle_point)





