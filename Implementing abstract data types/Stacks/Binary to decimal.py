from Stacks import Stack


# Basic binary converter
def convert_2_binary(integer):
    s = Stack()

    while integer != 0:
        rem = integer % 2
        integer = integer//2
        s.push(rem)

    binary = ''
    for x in range(s.size()):
        binary = binary + str(s.pop())

    return binary


# Test
# value = 10
# print(convert_2_binary(value))

# Universal converter
def base_converter(decimal, base):
    s = Stack()
    digits = "0123456789ABCDEF"

    while decimal != 0:
        rem = decimal % base
        decimal = decimal//base
        s.push(digits[rem])

    base_number = ''
    for x in range(s.size()):
        base_number = base_number + str(s.pop())

    return base_number


# Test
value = 100000
print(base_converter(value, 16))