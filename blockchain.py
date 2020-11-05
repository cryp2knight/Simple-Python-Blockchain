from datetime import datetime
import hashlib

class Block:
    block_no = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.block_no).encode('utf-8')
        )
        return h.hexdigest()

    def __repr__(self):
        return (
            f'Block Hash: {str(self.hash())}\n'
            f'Block #: {self.block_no}\n'
            f'Block Data: {self.data}\n'
            f'Hashes: {self.nonce}\n'
        )


class Blockchain:
    difficulty = 10
    max_nonce = 2**32
    target = 2 ** (256-difficulty)

    block = Block("Genesis")
    dummy = head = block

    def add(self, block):
        block.previous_hash = self.block.hash()
        block.block_no = self.block.block_no + 1
        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for _ in range(self.max_nonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                break
            else:
                block.nonce += 1
    
    def show(self):
        if not self.head:
            self.head = self.block
        while self.head:
            print(self.head)
            self.head = self.head.next
        

def _main():
    blockchain = Blockchain()
    # miningg
    for n in range(10):
        blockchain.mine(Block(f"Block {n+1}"))
        blockchain.show()
    #adding
    blockchain.add(Block('added block'))
    blockchain.show()
    blockchain.add(Block('added block2'))
    blockchain.show()


if __name__ == "__main__":
    _main()
