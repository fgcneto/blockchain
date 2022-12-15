from flask import Flask, jsonify, request

import bitcoinlib
import blockchain

app = Flask(__name__)
app.debug = True

blockchain = blockchain.Blockchain()


# [POST] /nodes/register para aceitar uma lista de novos nós no formato de URLs.
# Note que já existe uma variável do tipo conjunto (set) chamado nodes para armazenar os nós registrados.
@app.route('/nodes/register', methods=['POST'])
def register_new_miner():
    values = request.get_json()

    # obtem uma lista de nós
    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Forneça uma lista de nós válidos", 400

    # registra os nodes
    blockchain.nodes.add(nodes)

    response = {
        'message': 'Novo Nó foi adicionado.',
        'Total de Nó Mineradores': list(blockchain.nodes),
    }
    return jsonify(response), 200


# [GET] /nodes/resolve para executar o modelo de consenso, resolvendo conflitos
#  e garantindo que contém a cadeia de blocos correta.
# Basicamente o que deve ser feito pelo nó é solicitar a todos os seus nós registrados os seus respectivos blockchains.
#  Então deve-se conferir se o blockchain é válido, e, se for maior (mais longo) que o atual, deve substitui-lo.
@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    # Resolve conflitos para chegar so consenso
    conflicts = blockchain.resolveConflicts()

    if(conflicts):
        response = {
            'message': 'Chain substituída',
            'new_chain': blockchain.chain,
        }
        return jsonify(response), 200

    response = {
        'message': 'Chain mais longa',
        'chain': blockchain.chain,
    }
    return jsonify(response), 200


# [POST] /transactions/create para criar uma nova transação a ser incluída no próximo bloco.
# No corpo da requisicão HTTP, usando POST, inclua as informações necessárias para criação de uma nova transação.
@app.route('/transaction/create', methods=['POST'])
def new_transaction():

    values = request.get_json()
    required = ['sender', 'recipient', 'amount', 'timestamp', 'privWifKey']

    if not all(k in values for k in required):
        return 'Valores ausentes.'

    index = blockchain.createTransaction(
        sender=values['sender'],
        recipient=values['recipient'],
        amount=values['amount'],
        timestamp=values['timestamp'],
        privWifKey=values['privWifKey']
    )

    response = {
        'message': f'A transação será adicionada ao Bloco {index}',
    }
    return jsonify(response), 200


# [GET] /transactions/mempool para retornar a memory pool do nó.
@app.route('/transactions/mempool', methods=['GET'])
def mempool():
    return jsonify(blockchain.memPool), 200


# [GET] /mine para informar o nó para criar e minerar um novo bloco.
# Ou seja, um nó que for requisitado a partir desse end-point deve pegar todas as
# transações incluídas em seu memory pool, montar um bloco e minera-lo.
@app.route('/mine', methods=['GET'])
def mine():

    block = blockchain.createBlock()
    blockchain.mineProofOfWork(block)

    response = {
        'message': "New block.",
        'index': block['index'],
        'transactions': block['transactions'],
        'nonce': block['nonce'],
        'previousHash': block['previousHash'],
    }
    return jsonify(response), 200


# [GET] /chain para retornar o blockchain completo daquele nó.
@app.route('/chain', methods=['GET'])
def chain():
    response = {
        'chain': blockchain.chain,
        'tamanho': len(blockchain.chain),
    }
    return jsonify(response), 200
