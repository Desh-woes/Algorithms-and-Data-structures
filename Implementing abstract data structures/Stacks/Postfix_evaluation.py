from Stacks import Stack


def postfix_eval(string):
    op_stack = Stack()
    string_list = string.split()

    # Initialize variable for all potential operands (Letters and numbers)
    # letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '1234567890'

    for x in string_list:
        if x in numbers:
            op_stack.push(int(x))

        elif x in '*/-+':
            second_operand = op_stack.pop()
            first_operand = op_stack.pop()

            if x == '*':
                final_operand = second_operand*first_operand
            elif x == '-':
                final_operand = second_operand - first_operand
            elif x == '/':
                final_operand = second_operand/first_operand
            else:
                final_operand = second_operand+first_operand

            op_stack.push(final_operand)

    final_value = op_stack.pop()

    return final_value


# Test
test_value = '1 3 + 3 4 + *'
print(postfix_eval(test_value))