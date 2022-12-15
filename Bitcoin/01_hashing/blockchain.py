import hashlib
import json


class Blockchain(object):

    @staticmethod
    def generateHash(data):
        return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()


data = {
    'nome': "Walter White",
            'idade': 45
}
expected_hash = "ef9ef3225f42aed9de1581f19c729083fce7f764b94c3fdbfb261c27399d5fff"
data_hash = Blockchain.generateHash(data)
print(f'Dados: {data}')
print(f'Hash   gerado: {data_hash}')
print(f'Hash esperado: {expected_hash}')
print(f'Hashes iguais: ' + ('SIM!\n' if expected_hash == data_hash else 'NÃO!\n'))
