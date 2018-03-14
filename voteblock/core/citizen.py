from utils import generate_key_pair

class Citizen:
    def __init__(self, passphrase):
        (self.public_key, self.private_key) = generate_key_pair(passphrase)
