class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


# Activity
# Write a function rev_string(my_str) that uses a stack to reverse the characters in a string.
def rev_string(string):
    s = Stack()
    for i in string:
        s.push(i)

    reversed_string = ''
    for i in range(s.size()):
        reversed_string = reversed_string + s.pop()

    return reversed_string

# Test
# print(rev_string("Madagascar"))


# Activity 2
# The balanced parentheses problem
def check_par(symbol):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbol) and balanced:
        char = symbol[index]
        if char in '{[(':
            s.push(char)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, char):
                    balanced = False
        index += 1

    if balanced and s.is_empty():
        return True
    else:
        return False


def matches(first, last):
    opens = "([{"
    closes = ")]}"
    return opens.index(first) == closes.index(last)


# Test
symbol = '((((()))))'
print(check_par(symbol))

