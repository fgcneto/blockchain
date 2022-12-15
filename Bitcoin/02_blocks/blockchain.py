from copy import copy
import hashlib
import json
from datetime import datetime


class Blockchain(object):

    index = 0
    timestamp = 0
    nonce = 0
    merkleRoot = 0x0
    previousHash = ""
    transactions = []
    chain = []

    def __init__(self):
        self.chain = []
        self.memPool = []
        self.createGenesisBlock()

    @staticmethod
    def timestamp():
        return datetime.timestamp(datetime.now())

    @staticmethod
    def generateHash(data):
        return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()

    def createGenesisBlock(self):
        if Blockchain.index == 0:

            block = {
                'index': 0,
                'timestamp': {str(datetime.timestamp(datetime.now()))},
                'nonce': 0,
                'merkleRoot': 0x0,
                'previousHash': '0' * 64,
                'transactions': []
            }

            self.chain.append(block)
            Blockchain.index += 1
            return block

    @staticmethod
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def getBlockID(self):
        copy = self.last_block(self).copy()
        del copy['transactions']
        return self.generateHash(str(copy))

    def createBlock(self):
        block = {
            'index': self.index,
            'timestamp': str(datetime.timestamp(datetime.now())),
            'nonce': self.nonce,
            'merkleRoot': self.merkleRoot,
            'previousHash': self.getBlockID(self),
            'transactions': []
        }

        self.chain.append(block)
        Blockchain.index += 1
        return block

    def printChain(self):
        print(f'{self.chain}')


blockchain = Blockchain()
for x in range(0, 3):
    blockchain.createBlock()
blockchain.printChain()
