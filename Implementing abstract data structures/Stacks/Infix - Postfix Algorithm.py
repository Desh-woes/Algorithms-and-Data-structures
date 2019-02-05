# Import Stacks from existing document in the directory
from Stacks import Stack


# Define interface for infix to postfix function
def infix_to_postfix(string):
    # Initialize variable for all potential operands (Letters and numbers)
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '1234567890'

    # Create new stack ADT
    op_stack = Stack()

    # Split string into a list
    string_list = string.split()

    # Initialize output list where the new arrangement would be stored
    output_list = []

    # Initialize dictionary to hold all our precedents and their respective weights
    precedence = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

    # Loop through all the elements in our slitted list of strings
    for x in string_list:

        # If element is an operand, simply add it to our output list since we do not want to change the position of
        # our operands
        if x in letters or x in numbers:
            output_list.append(x)

        # Else if the element is a left bracket, add it to the top of our stack in anticipation of a closing bracket
        elif x == '(':
            op_stack.push(x)

        # If element is a closing bracket, and our stack is not empty, pop all elements in the stack until we hit the
        # Closing bracket
        elif x == ')' and not op_stack.is_empty():
            top = op_stack.pop()

            # Append all elements in our stack to our output list until we hit our opening bracket.
            while top != '(':
                output_list.append(top)
                top = op_stack.pop()

        # Else if we hit any other operator:
        elif x in precedence.keys():

            # Remove all elements before it which have a higher or equal precedent.
            while not op_stack.is_empty() and precedence[op_stack.peek()] >= precedence[x]:
                # Append those elements to our output list
                output_list.append(op_stack.pop())

            # Then push our current symbol.
            op_stack.push(x)

    # Eventually add the remaining elements in our stack to our output list
    while not op_stack.is_empty():
        top = op_stack.pop()
        output_list.append(top)

    # Return our output list as a string
    return " ".join(output_list)


# test
infix = "( A + B ) * ( C + D )"
infix2 = "( A + B ) * C - ( D - E ) * ( F + G)"
print(infix_to_postfix(infix))