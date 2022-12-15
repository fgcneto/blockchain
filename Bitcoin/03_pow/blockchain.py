import hashlib
import json
import copy
from time import time

# Quantidade de zeros (em hex) iniciais no hash considerado válido (resposta ao puzzle criptográfico no proof-of-work).
DIFFICULTY = 4


class Blockchain(object):
    '''Classe utilizada para representar um blockchain privado baseado no protocolo Bitcoin.'''

    def __init__(self):
        self.chain = []
        self.memPool = []
        self.createGenesisBlock()

    def createGenesisBlock(self):
        '''Cria, minera e retorna o bloco gênesis do blockchain. Chamado somente no construtor.'''
        genesis_block = self.createBlock()
        self.mineProofOfWork(self.prevBlock)
        return genesis_block

    def createBlock(self):
        '''Cria um novo bloco, inclui todas as transações pendentes e adiciona ao chain. O bloco ainda não tem nonce válido.'''
        block = {
            'index': len(self.chain),
            'timestamp': int(time()),
            'transactions': self.memPool,
            'merkleRoot': '0'*64,
            'nonce': 0,
            'previousHash': self.getBlockID(self.chain[-1]) if (len(self.chain)) else '0'*64
        }
        self.memPool = []
        self.chain.append(block)
        return block

    def mineProofOfWork(self, block):
        '''Retorna um nonce válido para o bloco passado como argumento.'''
        nonce = 0
        while self.isValidProof(block, nonce) is False:
            nonce += 1
        return nonce

    @staticmethod
    def isValidProof(block, nonce):
        '''Retorna `True` caso o nonce passado como argumento seja válido para o block passado como argumento, `False` caso contrário.'''
        block['nonce'] = nonce
        provavelHash = Blockchain.getBlockID(block)
        return provavelHash[:DIFFICULTY] == '0' * DIFFICULTY

    @staticmethod
    def generateHash(data):
        '''Retorna a hash SHA256 dos dados passados como argumento.'''
        blkSerial = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(blkSerial).hexdigest()

    @staticmethod
    def getBlockID(block):
        '''Retorna o ID do bloco passado como argumento. O ID de um bloco é o hash do seu cabeçalho.'''
        blockCopy = copy.copy(block)
        blockCopy.pop("transactions", None)
        return Blockchain.generateHash(blockCopy)

    def printChain(self):
        for block in self.chain:
            print('--------------------------------------------------------------------')
            previousBlock = copy.copy(block)
            del (previousBlock["transactions"])
            previousHash = self.generateHash(previousBlock)
            print(previousHash)
            print('*********')
            print('Indice: ')
            print(block['index'])
            print('*********')
            print('timestamp: ')
            print(block['timestamp'])
            print('*********')
            print('nonce')
            print(block['nonce'])
            print('*********')
            print('merkleRoot')
            print(block['merkleRoot'])
            print('*********')
            print('Hash do ultimo bloco: ')
            print(block['previousHash'])
            print('[|]')
            print(' | ')
            print('[|]')

    @property
    def prevBlock(self):
        '''Retorna o último bloco da chain.'''
        return self.chain[-1]


# Teste local, fique a vontade para modificar.
blockchain = Blockchain()
for x in range(0, 4):
    blockchain.createBlock()
    blockchain.mineProofOfWork(blockchain.prevBlock)
    blockchain.printChain()

for x in blockchain.chain:
    print('[Bloco #{} : {}] Nonce: {} | É válido? {}'.format(x['index'],
          Blockchain.getBlockID(x), x['nonce'], Blockchain.isValidProof(x, x['nonce'])))
