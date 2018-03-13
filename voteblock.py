from datetime import datetime
from pprint import pprint
import hashlib

def hash_block(block):
    hash_object = hashlib.sha256(bytearray(block))
    return hash_object.hexdigest()

def validate_block_chain(bc, difficulty):
    target = "0" * difficulty
    for i in range(1, len(bc)):
        if bc[i].hash != bc[i].calculate_hash():
            return False
        if bc[i-1].hash != bc[i].previous:
            return False
        if not bc[i].hash.startswith(target):
            return False
    return True

class Block:
    def __init__(self, dat, prev = "0"):
        self.nonce = 0
        self.data = dat
        self.previous = prev
        self.timestamp = str(datetime.utcnow())
        self.hash = self.calculate_hash()

    def get_block_string(self):
        return self.data + self.timestamp + self.previous + str(self.nonce)

    def calculate_hash(self):
        return hash_block(self.get_block_string())

    def mine_block(self, difficulty):
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()

difficulty = 6

block_chain = []

block_chain.append(Block("Block 1"))
block_chain[0].mine_block(difficulty)
print("Mined Block 1")

block_chain.append(Block("Block 2", block_chain[-1].hash))
block_chain[1].mine_block(difficulty)
print("Mined Block 2")

block_chain.append(Block("Block 3", block_chain[-1].hash))
block_chain[2].mine_block(difficulty)
print("Mined Block 3")

print("Block chain is valid" if validate_block_chain(block_chain, difficulty) else "Block chain is invalid")
for b in block_chain:
    pprint(b.__dict__)
