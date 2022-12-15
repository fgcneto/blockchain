# Descrição das atividade

# Atividade: Hashing (01-hashing)

Esta atividade tem como objetivo implementar o primeiro método no desenvolvimento do nosso **blockchain**. Este método estático será amplamente utilizado em várias etapas do processo, uma vez que _hashing_ é uma das técnicas essenciais para o funcionamento deste modelo de blockchain.

## Instalação

Baixe o arquivo `./blockchain.py` para obter o _boilerplate_ para esta atividade. Caso seja necessário, utilize o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar os módulos necessários. Todos os _boilerplates_ são compatíveis com o Python 3+.

## Descrição e Dicas sobre Hash e como implementar

Implementa da geração de Hash que retorna uma string _hash_ **SHA256** .

```python
@staticmethod
def generateHash(data):
```

Confira a documentação do hashlib [https://docs.python.org/3/library/hashlib.html] para verificar como utilizar a função SHA256.

Usar `json.dumps()` do módulo `json` para serializar o objeto de entrada em uma string no formato JSON antes, e lembrar de manter a estrutura sempre ordenada (`sort_keys=True`). Assim temos a garantia de que a função irá retornar o mesmo _hash_ independentemente da ordem em que as chaves são apresentadas, crucial para validação de algumas estruturas de nosso blockchain.

```python
json.dumps(data, sort_keys=True)
```

# Atividade: Blocos (`02-blocks`)

Esta atividade tem como objetivo implementar o modelo de dados responsável por representar um bloco em nosso blockchain, além de implementar métodos responsáveis pela criação destes blocos.

## Descrição

A estrutura/objeto/dicionário abaixo representa um bloco.

```python
{
    'index': 2,
    'timestamp': 1506057125,
    'nonce': 324984,
    'merkleRoot': "13c8bbf1dde38d5f86bfc48a5c027df0d8eb19c8a647de49976755e1b35b31ca",
    'previousHash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",
    'transactions': [] # Por enquanto usar lista vazia.
}
```

Onde:

- `index`: índice do bloco, que representa a profundidade do bloco no blockchain (o bloco genesis tem `index` 0);
- `timestamp` : data (formato unix, somente segundos) de criação do novo bloco;
- `nonce` : Um número arbitrário que mineradores alteram para modificar o hash do cabeçalho para produzir um hash menor ou igual ao limite de destino;
- `merkleRoot` : Uma raiz Merkle é o hash de todos os hashes de todas as transações que fazem parte de um bloco em uma rede blockchain;
- `previousHash` : _hash_ do cabeçalho do bloco anterior. O cabeçalho é formado pelos campos `index`, `timestamp`, `nonce`, `merkleRoot` e `previousHash`. O cálculo do _hash_ do bloco anterior a partir do dicionário que representa a estrutura, SEM o atributo `transactions`, que não faz parte do cabeçalho;
- `transactions` : lista de transações incluídas no bloco;

## A função createBlock() realiza a criação dos blocos na Blockchain

```python
def createBlock()
```

## A função createGenesisBlock() é responsável por criar o Genesis Block, bloco que não possui antecedentes

```python
def createGenesisBlock()
```

## Descrição da função getBlockID(block)

```python
def getBlockID(block)
```

Método estático auxiliar para gerar o identificador (ID) de um bloco passado como parâmetro. Lembrando que o ID de um bloco é a _hash_ (no nosso caso com a função SHA256) do **cabeçalho** de um bloco. Na nossa implementação, fazem parte do cabeçalho de um bloco os campos: `index`, `timestamp`, `nonce`, `merkleRoot` e `previousHash`.

- `chain` : uma lista de blocos, representando o blockchain; os blocos são armazenados nessa lista de maneira ordenada.
- `memPool` : o _memory pool_, responsável por armazenar, temporariamente, transações que ainda não foram incluídas em um bloco;

## Mas dicas em:

- [Documentação para gerenciar Timestamps em Python](https://docs.python.org/3/library/time.html)

# Atividade: Proof-of-Work (`03-pow`)

## Método `mineProofOfWork(block)`

O método `mineProofOfWork(block)` retorna e atribuir um _nonce_ válido para o último bloco criado. `DIFFICULTY` é a dificuldade FIXA, que representa a quantidade de zeros em hexadecimais exigidas no início do _hash_ do cabeçalho do bloco. De maneira sucinta, todo bloco criado deverá passar pelo processo de mineração para que seja válido. A assinatura do método é definida como:

```python
def mineProofOfWork(self, block):
```

## Método isValidProof(block, nonce)

O método `isValidProof(block, nonce)`, retorna `True` caso o `nonce` passado como argumento seja válido para o bloco, o `block` também é passado como argumento.

```python
def isValidProof(block, nonce):
```

A dificuldade definida para essa atividade é que o _hash_ do cabeçalho do bloco deve ser menor que o alvo (_target_) abaixo:

`alvo = 0x0001000000000000000000000000000000000000000000000000000000000000`

Isso quer dizer que o _hash_ encontrado deve ter um prefixo de quatro caracteres hexadecimais 0's. Exemplos:

- **[INVÁLIDO]** 00078112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
- **[INVÁLIDO]** 0001e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d
- **[VÁLIDO]** 00002c03a9507ae265ecf5b5356885a53393a2029d241394997265a1a25aefc6
