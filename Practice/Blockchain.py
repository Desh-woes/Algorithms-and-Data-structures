import hashlib
from datetime import datetime


class Block:
    # Define constructor
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    # Define hashing function to hash the given data
    def calc_hash(self):
        sha = hashlib.sha3_256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    # Function to get the hash
    def get_hash(self):
        return self.hash

    # Function to change the data in a node and update the hash
    def change_data(self, data):
        self.data = data
        self.hash = self.calc_hash()

    # Update the string method
    def __repr__(self):
        return 'previous hash: ' + str(self.previous_hash) + '\ncurrent hash: ' + self.hash + '\n' * 2


# test case 1
data1 = "I've got 100000 bitcoins."
data2 = "But satoshi has 100000 of them."
data3 = "don't worry, bitcoin is going down"
data4 = "Where are the transactions listed?"

block1 = Block(data1, '0')
block2 = Block(data2, block1.get_hash())
block3 = Block(data3, block2.get_hash())
block4 = Block(data4, block3.get_hash())

assert (block2.previous_hash == block1.calc_hash())
assert (block3.previous_hash == block2.calc_hash())
assert (block4.previous_hash == block3.calc_hash())

print(block1, block2, block3, block4)