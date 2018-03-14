from hashable import Hashable
from datetime import datetime

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

class Block(Hashable):
    def __init__(self, dat, prev = "0"):
        self.nonce = 0
        self.data = dat
        self.previous = prev
        self.timestamp = str(datetime.utcnow())
        self.hash = self.calculate_hash()

    def get_block_string(self):
        return self.data + self.timestamp + self.previous + str(self.nonce)

    def mine_block(self, difficulty):
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()
