from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Signature import DSS
from utils import hash_str

class Hashable:
    def calculate_hash(self):
        return hash_str(self.get_block_string())

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
