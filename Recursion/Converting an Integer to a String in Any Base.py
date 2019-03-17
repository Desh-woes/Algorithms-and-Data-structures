# Recursive algorithm to keep reducing the integer to it's base case and return a string in the new base
def convert_tostr(number, base):
    conversion_string = "0123456789ABCDEF"
    if number < base:
        return conversion_string[number]

    else:
        return convert_tostr(number//base, base) + conversion_string[number%base]


# Test parameters
print(convert_tostr(7, 8))
