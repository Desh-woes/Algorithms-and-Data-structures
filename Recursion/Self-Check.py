# Task 1
# Write a function that takes a string as a parameter and returns a new string that is the reverse of the old string.
def reverse_str(new_str):
    # Turn string into a list to make iteration easier
    str_list = list(new_str)

    if len(new_str) == 1:
        return new_str[0]

    else:
        return reverse_str(''.join(str_list[1:])) + str_list[0]


# Test Params for reversing strings
test_string = "Oluwarotimi"
print(reverse_str(test_string))
