class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        self.size += 1

    def get_size(self):
        return self.size


def union(llist_1, llist_2):
    union_set = set()
    union_linked_list = LinkedList()

    # Loop through the first list and add it's elements to the union set and the union ll
    pointer = llist_1.head
    while pointer is not None:
        if pointer.value not in union_set:
            union_set.add(pointer.value)
            union_linked_list.append(pointer.value)
        pointer = pointer.next

    # loop through the second list now and append anything not in the first set
    pointer = llist_2.head
    while pointer is not None:
        if pointer.value not in union_set:
            union_set.add(pointer.value)
            union_linked_list.append(pointer.value)
        pointer = pointer.next

    # Return the union linked list
    return union_linked_list


def intersection(llist_1, llist_2):
    intersection_set = set()
    intersection_linked_list = LinkedList()

    # Loop through the first list and add it's elements to the union set but not to the union linked list
    pointer = llist_1.head
    while pointer is not None:
        if pointer.value not in intersection_set:
            intersection_set.add(pointer.value)
        pointer = pointer.next

    # Loop through the second list and the check for things that are not in the intersection set.
    pointer = llist_2.head
    while pointer is not None:
        if pointer.value in intersection_set:
            intersection_linked_list.append(pointer.value)
            intersection_set.remove(pointer.value)
        pointer = pointer.next

    return intersection_linked_list


# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))

