from hashable import Hashable
from datetime import datetime



class Block(Hashable):
    def __init__(self, data, block_chain, previous):
        self.nonce = 0
        self.data = data
        self.previous = previous
        self.timestamp = str(datetime.utcnow())
        self.hash = self.calculate_hash()
        self.target = "0" * block_chain.difficulty

    def get_block_string(self):
        return self.data + self.timestamp + self.previous + str(self.nonce)

    def mine(self):
        while not self.is_mined():
            self.nonce += 1
            self.hash = self.calculate_hash()
        return True

    def is_mined(self):
        return True if self.hash.startswith(self.target) else False

class BlockChain:
    def __init__(self, difficulty):
        self.chain = []
        self.difficulty = difficulty

    def create_block(self, dat, prev = "0"):
        self.chain.append(Block(dat, self, prev))
        return len(self.chain) - 1

    def get_latest_mined_block_hash(self):
        for x in reversed(range(len(self.chain))):
            if self.chain[x].is_mined():
                return self.chain[x].hash
        return None

    def mine_block(self, index):
        if index < len(self.chain) and index >= 0:
            return self.chain[index].mine()
        return False

    def validate(self):
        target = "0" * self.difficulty
        bc = self.chain
        for i in range(1, len(bc)):
            if bc[i].hash != bc[i].calculate_hash():
                return False
            if bc[i-1].hash != bc[i].previous:
                return False
            if not bc[i].hash.startswith(target):
                return False
        return True
