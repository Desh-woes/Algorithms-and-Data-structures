# Implementing the node class
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# Create the node wrapper
class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

    # Implement append function
    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node
        self.tail.next = cur.next

    # Implement count/len function
    def length(self):
        cur = self.head
        count = 0
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
                cur = cur.next
                if cur_index == index:
                    return cur.data
                else:
                    cur_index += 1

# Test params
# test = LinkedList()
# test.append(2)
# test.append(3)


# Singly linked circular list
class CircularLinkedList:
    def __init__(self, data=None):
        self.cur = Node(data)
        self.cur.next = self.cur

    # Appending in a Circular linked list
    def append(self, data):
        new_node = Node(data)
        cur_node = self.cur
        while cur_node.next != self.cur:
            cur_node = cur_node.next
        new_node.next = cur_node.next
        cur_node.next = new_node

    # Search for a given number in the list
    def search(self, data):
        new_node = Node(data)
        cur_node = self.cur
        while cur_node.next != self.cur:
            if cur_node.next.data == new_node.data:
                return cur_node.data
            cur_node = cur_node.next
        return None


# Test params Circular list
test = CircularLinkedList()
test.append(1)
test.append(2)
test.append(3)
test.append(4)
print(test.cur.next.data)
print(test.search(2))