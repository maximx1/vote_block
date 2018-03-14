from hashable import Hashable
from datetime import datetime

class Vote(Hashable):
    def __init__(self, voter_key, votee_key, inputs):
        self.voter_key = voter_key
        self.votee_key = votee_key
        self.inputs = inputs
        self.timestamp = str(datetime.utcnow())
        self.cast_vote_count = 1
        self.sequence = 0

    def get_block_string(self):
        sequence += 1
        return self.voter_key + self.votee_key + self.timestamp + str(self.cast_vote_count) + str(self.sequence)

    def get_signature_data_string(self):
        return self.voter_key + self.votee_key + str(self.cast_vote_count)

    def sign_vote(self, private_key, passphrase):
        data = self.get_signature_data_string()
        self.signature = self.create_ecc_sig(private_key, passphrase, data)

    def validate_signature(self):
        data = self.get_signature_data_string()
        return self.verify_ecc_sig(self.voter_key, data, self.signature)
