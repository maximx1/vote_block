from pprint import pprint
from voteblock.core.citizen import Citizen
from voteblock.core.vote import Vote
from voteblock.core.blockchain import BlockChain

difficulty = 4

# voter = Citizen("snicklefritz")
# print(voter.private_key)
# print(voter.public_key)
# votee = Citizen("ztirfelkcins")
# vote = Vote(voter.public_key, votee.public_key, None)
# vote.sign_vote(voter.private_key, "snicklefritz")
# print("Transaction sig is valid" if vote.validate_signature() else "Transaction sig is invalid")

bc = BlockChain(difficulty)

bc.create_block("Block 1")
bc.mine_block(0)
print("Mined Block 1")

bc.create_block("Block 2", bc.get_latest_mined_block_hash())
bc.mine_block(1)
print("Mined Block 2")

bc.create_block("Block 3", bc.get_latest_mined_block_hash())
bc.mine_block(2)
print("Mined Block 3")

print("Block chain is valid" if bc.validate() else "Block chain is invalid")
for b in bc.chain:
    pprint(b.__dict__)
