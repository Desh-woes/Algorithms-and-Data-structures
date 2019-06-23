class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """

    if head is None:
        return None

    # Referenced to the head and tails of the even nodes
    even_head = None
    even_tail = None

    # Referenced to the head and tail of the odd nodes
    odd_head = None
    odd_tail = None

    while head is not None:
        # temp to keep reference to the other part of the linked list
        temp_head = head.next

        # Check if the current value is even
        if head.data % 2 == 0:
            # Check if there is a current head
            if even_head is None:
                even_head = head
                even_tail = even_head
            else:
                even_tail.next = head
                even_tail = even_tail.next

        # Check if the current value is odd
        else:
            if odd_head is None:
                odd_head = head
                odd_tail = odd_head
            else:
                odd_tail.next = head
                odd_tail = odd_tail.next

        # Clear head
        head.next = None

        # Assign new head
        head = temp_head

    # check if there was any odd value
    if odd_head is None:
        return even_head
    else:
        odd_tail.next = even_head
        return odd_tail


def skip_i_delete_j(head, i, j):
    """
    :param: head - head of linked list
    :param: i - first `i` nodes that are to be skipped
    :param: j - next `j` nodes that are to be deleted
    return - return the updated head of the linked list
    """
    counter = 1
    temp_stop = None
    curr = head
    while curr is not None:
        if counter == i:
            temp_stop = curr

        if counter == i+j:
            temp_stop.next = curr.next
            counter = 1
        curr = curr.next
        counter += 1
    return head
