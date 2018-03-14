from pprint import pprint
from voteblock.core.citizen import Citizen
from voteblock.core.vote import Vote
from voteblock.core.blockchain import Block, validate_block_chain
import hashlib


difficulty = 6

voter = Citizen("snicklefritz")
print(voter.private_key)
print(voter.public_key)
votee = Citizen("ztirfelkcins")
vote = Vote(voter.public_key, votee.public_key, None)
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
