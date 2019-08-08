import sys
from queue import PriorityQueue


# Define the tree node class
class Node:
    def __init__(self, value=None, data = None):
        self.value = value
        self.data = data
        self.left = None
        self.right = None

    # Overwrite the equal to comparator
    def __eq__(self, other):
        return self.value == other.value

    # Overwrite the less than comparator
    def __lt__(self, other):
        return self.value < other.value

    # Overwrite the greater than comparator
    def __gt__(self, other):
        return self.value > other.value

    # Overwrite the string method for printing nodes
    def __str__(self):
        if self.data is None:
            return "parent Node" + ":" + str(self.value)
        return self.data + ":" + str(self.value)


# Function to generate a code table given a tree
def gen_code_table(root_node, string_so_far, code_table):
    if (root_node.left is None) and (root_node.right is None):
        code_table[root_node.data] = string_so_far
    else:
        if root_node.left is not None:
            gen_code_table(root_node.left, string_so_far+"0", code_table)

        if root_node.right is not None:
            gen_code_table(root_node.right, string_so_far+"1", code_table)


# Function to encode data
def huffman_encoding(data):
    # Create a code table
    freq_table = {}
    for char in data:
        if char in freq_table.keys():
            freq_table[char] += 1
        else:
            freq_table[char] = 1

    # Add elements into the priority queue from the code table
    freq_pq = PriorityQueue()
    for _data, value in freq_table.items():
        new_node = Node(data=_data, value=value)
        freq_pq.put(new_node)

    root_node = None
    while not freq_pq.empty():
        node1 = freq_pq.get()

        if not freq_pq.empty():
            node2 = freq_pq.get()

            new_node = Node(value=node1.value+node2.value)
            new_node.left = node1
            new_node.right = node2
            freq_pq.put(new_node)
        else:
            root_node = node1

    code_table = {}
    gen_code_table(root_node, "", code_table)

    coded_data = ""
    for i in data:
        coded_data += code_table[i]

    return coded_data, root_node


# Function to decode an encoded message
def huffman_decoding(data, root_node):
    main_root = root_node
    output_string = ""
    for i in data:
        if i == "1":
            root_node = root_node.right
        else:
            root_node = root_node.left

        if (root_node.left is None) and (root_node.right is None):
            output_string += root_node.data
            root_node = main_root

    return output_string


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "Bitcoin[a] (₿) is a cryptocurrency. It is a decentralized digital currency without a central" \
                       " bank or single administrator that can be sent from user to user on the peer-to-peer bitcoin" \
                       " network without the need for intermediaries.[8] Transactions are verified by network nodes" \
                       " through cryptography and recorded in a public distributed ledger called a blockchain. " \
                       "Bitcoin was invented by an unknown person or group of people using the name Satoshi Nakamoto[15]" \
                       " and was released as open-source software in 2009.[16] Bitcoins are created as a reward for a " \
                       "process known as mining. They can be exchanged for other currencies, products, and services.[17]" \
                       " Research produced by University of Cambridge estimates that in 2017, there were 2.9 to 5.8 million" \
                       " unique users using a cryptocurrency wallet, most of them using bitcoin.[18]"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))