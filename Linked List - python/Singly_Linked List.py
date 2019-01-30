# Implementing the node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create the node wrapper
class LinkedList:
    def __init__(self, data=None):
        if data is None:
            self.head = data

        else:
            self.head = Node(data)
            self.tail = self.head

    # Implement append function
    def append(self, data):
        new_node = Node(data)
        cur = self.head

        if cur is not None:
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
            self.tail = cur.next

        else:
            self.head = new_node

    # Implement count/len function
    def length(self):
        cur = self.head
        count = 0
        if cur is not None:
            count = 1
            while cur.next is not None:
                count += 1
                cur = cur.next

        return count

    # Implement Index get function
    def get(self, index):
        if index >= self.length():
            print('You have given an index that is out of range')
            return None
        else:
            cur_index = 0
            cur = self.head
            while True:
                if cur_index == index:
                    return cur.data
                else:
                    cur = cur.next
                    cur_index += 1

    # Function to display the contents of the linked list
    def display(self):
        cur = self.head
        while cur.next is not None:
            print(cur.data)
            cur = cur.next
        print(cur.data)

    # Function to reverse the contents of the linked list
    def reverse(self):
        # Current is a pointer to head
        cur = self.head

        # If out pointer is null, then our list is empty so return it
        if cur is None:
            return cur

        # Else if our list is not empty
        else:

            # While we are not on our last element
            while cur.next is not None:
                # Store our next value as temp
                temp = cur.next

                # Switching variable in position 1
                if cur == self.head:
                    cur.next = None
                    temp_2 = temp.next
                    temp.next = cur
                    self.head = temp
                    cur = temp_2

                # Switching variables in other positions
                else:
                    cur.next = self.head
                    self.head = cur
                    cur = temp

            # Switching the last variable
            cur.next = self.head
            self.head = cur


# Test params
test = LinkedList(1)
test.append(2)
test.append(3)
test.display()
# print(test.get(0))
test.reverse()
test.display()