# Initialize the doubly linked list class
class DoublyLinkedList:
    def __init__(self, key=None, value=None):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None


# Initialize the LRU-Cache class
class LRUCache:
    # Constructor to initialize an LRU cache
    def __init__(self, capacity):
        # Total capacity
        self.max_cap = capacity

        # Head Node of the doubly Linked List
        self.head_node = DoublyLinkedList()

        # Tail node of the doubly linked List
        self.tail_node = DoublyLinkedList()

        # Assign head and tail nodes
        self.tail_node.prev = self.head_node
        self.head_node.next = self.tail_node

        # Map that stores the keys and the values stored in the cache
        self.hash_map = {}  # Stores the key to node mapping

    # Define the set operator for the cache
    def set(self, key, value):
        # Check if the key is already in the hashmap
        if key in self.hash_map.keys():
            curr_node = self.hash_map[key]
            curr_node.value = value

            # Remove the curr_node
            curr_node.prev.next = curr_node.next
            curr_node.next.prev = curr_node.prev

            # Add the current node to the head of the node
            curr_node.next = self.head_node.next
            self.head_node.next = curr_node
            curr_node.next.prev = curr_node
            curr_node.prev = self.head_node

        # Check if the Hash map is still within capacity
        elif len(self.hash_map) < self.max_cap:
            # Create new doubly linked list node
            new_node = DoublyLinkedList(key, value)

            # Add node to the front of the doubly linked List
            new_node.next = self.head_node.next
            self.head_node.next = new_node
            new_node.next.prev = new_node
            new_node.prev = self.head_node

            # Add node to the hash map
            self.hash_map[key] = new_node

        else:
            # Remove the element at the end of the doubly linked list
            curr_node = self.tail_node.prev
            curr_node.next.prev = curr_node.prev
            curr_node.prev.next = curr_node.next
            remove_key = curr_node.key
            del self.hash_map[remove_key]

            # Create new doubly linked list node
            new_node = DoublyLinkedList(key, value)

            # Add node to the front of the doubly linked List
            new_node.next = self.head_node.next
            self.head_node.next = new_node
            new_node.next.prev = new_node
            new_node.prev = self.head_node

            # Add node to the hash map
            self.hash_map[key] = new_node

    def get(self, key):
        if key not in self.hash_map:
            print(-1)
        else:
            # Update its position
            curr_node = self.hash_map[key]

            # Remove the curr_node
            curr_node.prev.next = curr_node.next
            curr_node.next.prev = curr_node.prev

            # Add the current node to the head of the node
            curr_node.next = self.head_node.next
            self.head_node.next = curr_node
            curr_node.next.prev = curr_node
            curr_node.prev = self.head_node

            print(curr_node.key)


our_cache = LRUCache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

our_cache.get(3)
our_cache.get(6)


# test case 1
print("--------------------------------------------------------------------------------------------------------")
our_cache = LRUCache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.get(1)  # returns 1
our_cache.get(2)  # returns 2
our_cache.get(9)  # returns -1
our_cache.set(5, 5)
our_cache.set(6, 6)
our_cache.get(3)  # returns -1 because key 3 was thrown out
our_cache.set(7, 7)
our_cache.get(4)  # 4 is thrown out
print('\n')

# test case 2
print("--------------------------------------------------------------------------------------------------------")
our_cache = LRUCache(5)
our_cache.set(1, 1)
our_cache.get(2)  # returns -1
our_cache.set(1, 11111)
our_cache.get(1)  # overriding a value, returns 11111


# test case 3
# different keys may have the same value, but same keys may not have the same values
print("--------------------------------------------------------------------------------------------------------")
our_cache = LRUCache(5)
our_cache.set(12343545, 1)
our_cache.set(564, 1)
our_cache.set(456, 1)
our_cache.set(678, 1)
our_cache.get(1)  # -1
our_cache.get(12343545)  # 1
our_cache.get(564)  # 1
our_cache.get(678)  # 1
our_cache.set(1, 564)
our_cache.set(1, 456)
our_cache.set(1, 678)
our_cache.get(1)  # 678
