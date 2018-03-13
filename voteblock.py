from datetime import datetime
from pprint import pprint
from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Signature import DSS
import hashlib

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

def generate_key_pair(passphrase):
    key = ECC.generate(curve='P-256')
    private_key = key.export_key(passphrase=passphrase, format='PEM', protection="PBKDF2WithHMAC-SHA1AndAES128-CBC")
    public_key = key.public_key().export_key(format='PEM')
    return (public_key, private_key)

class Citizen:
    def __init__(self, passphrase):
        (self.public_key, self.private_key) = generate_key_pair(passphrase)

class Hashable:
    def calculate_hash(self):
        return self.hash_block(self.get_block_string())

    def hash_block(self, block):
        hash_object = hashlib.sha256(bytearray(block))
        return hash_object.hexdigest()

    def create_ecc_sig(self, private_key, passphrase, data):
        key = ECC.import_key(private_key, passphrase)
        converted_data = bytearray(data)
        hashed_data = SHA256.new(converted_data)
        signer = DSS.new(key, 'fips-186-3')
        return signer.sign(hashed_data)

    def verify_ecc_sig(self, public_key, data, signature):
        key = ECC.import_key(public_key)
        hashed_message = SHA256.new(data)
        verifier = DSS.new(key, 'fips-186-3')
        try:
            verifier.verify(hashed_message, signature)
            return True
        except ValueError:
            return False

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

class Vote(Hashable):
    def __init__(self, voter, votee, inputs):
        self.voter = voter
        self.votee = votee
        self.inputs = inputs
        self.timestamp = str(datetime.utcnow())
        self.cast_vote_count = 1
        self.sequence = 0

    def get_block_string(self):
        sequence += 1
        return self.voter + self.votee + self.timestamp + str(self.cast_vote_count) + str(self.sequence)

    def get_signature_data_string(self):
        return str(self.voter) + str(self.votee) + str(self.cast_vote_count)

    def sign_vote(self, private_key, passphrase):
        data = self.get_signature_data_string()
        self.signature = self.create_ecc_sig(private_key, passphrase, data)

    def validate_signature(self):
        data = self.get_signature_data_string()
        return self.verify_ecc_sig(self.voter.public_key, data, self.signature)

#print(Citizen("dddd").__dict__)

difficulty = 6

voter = Citizen("snicklefritz")
votee = Citizen("ztirfelkcins")
vote = Vote(voter, votee, None)
vote.sign_vote(voter.private_key, "snicklefritz")
print("Transaction sig is valid" if vote.validate_signature() else "Transaction sig is invalid")

#
# block_chain = []
#
# block_chain.append(Block("Block 1"))
# block_chain[0].mine_block(difficulty)
# print("Mined Block 1")
#
# block_chain.append(Block("Block 2", block_chain[-1].hash))
# block_chain[1].mine_block(difficulty)
# print("Mined Block 2")
#
# block_chain.append(Block("Block 3", block_chain[-1].hash))
# block_chain[2].mine_block(difficulty)
# print("Mined Block 3")
#
# print("Block chain is valid" if validate_block_chain(block_chain, difficulty) else "Block chain is invalid")
# for b in block_chain:
#     pprint(b.__dict__)
