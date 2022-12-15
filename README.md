[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://github.com/fgcneto/bitcoin/blob/main/blockchain.py)

## Descrição da API - Flash

### A api possui 5 _end-points_:

- **[POST]** `/transactions/create` - cria uma nova transação a ser incluída no próximo bloco. No corpo da requisicão HTTP, usando POST,deverá conter as informações necessárias para criação de uma nova transação.
- **[GET]** `/transactions/mempool` para retornar a _memory pool_ do nó.
- **[GET]** `/mine` para informar o nó para criar e minerar um novo bloco. Ou seja, um nó que for requisitado a partir desse end-point deve pegar todas as transações incluídas em seu memory pool, montar um bloco e minera-lo.
- **[GET]** `/chain` para retornar o blockchain completo daquele nó.
- **[POST]** `/nodes/register` para aceitar uma lista de novos nós no formato de URLs. Note que já existe uma variável do tipo conjunto (_set_) chamado `nodes` para armazenar os nós registrados.
- **[GET]** `/nodes/resolve` para executar o modelo de consenso, resolvendo conflitos e garantindo que contém a cadeia de blocos correta. Basicamente o que deve ser feito pelo nó é solicitar a todos os seus nós registrados os seus respectivos blockchains. Então deve-se conferir se o blockchain é válido, e, se for maior (mais longo) que o atual, deve substitui-lo.

<table style="width:100%">
  
  <tr>
    <td colspan="2"><strong>Apresentação do Material Auxiliar de EStudos</strong></td>
  </tr>
  <tr>
    <td>Slides</td>
    <td><a target="_blank" href="https://github.com/fgcneto/blockchain/raw/main/slides/00-presentation.pdf"><img src="https://img.shields.io/badge/-Slides-008ED2?style=flat-square&logo=adobe-acrobat-reader"></a></td>
  </tr>
  <tr>
    <td>Bibliografia</td>
    <td><a target="_blank" href="https://github.com/bitcoinbook/bitcoinbook">Mastering Bitcoin</a> <em>por A. Antonopoulos</em><br><a target="_blank" href="https://github.com/ethereumbook/ethereumbook">Mastering Ethereum</a> <em>por A. Antonopoulos</em></td>
  </tr>
  <tr>
    <td colspan="2"><strong>O protocolo Bitcoin: visão geral</strong></td>
  </tr>
  <tr>
    <td>Slides</td>
    <td><a target="_blank" href="https://github.com/fgcneto/blockchain/raw/main/slides/01-bitcoin-overview.pdf"><img src="https://img.shields.io/badge/-Slides-008ED2?style=flat-square&logo=adobe-acrobat-reader"></a></td>
  </tr>
  <tr>
    <td>Leitura complementar</td>
    <td>MB Capítulos <a target="_blank" href="https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch01.asciidoc">1</a> e <a target="_blank" href="https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch02.asciidoc">2</a></td>
  </tr>
  <tr>
    <td>Material complementar</td>
    <td><a target="_blank" href="https://bitcoin.org/bitcoin.pdf">White paper</a> por <em>Satoshi Nakamoto</em><br>
    <a target="_blank" href="https://learnmeabitcoin.com/">How does Bitcoin work?</a> por <em>Greg W</em></td>
  </tr>

  <tr>
    <td colspan="2"><strong>Do Bitcoin ao Blockchain</strong></td>
  </tr>
  <tr>
    <td>Slides</td>
    <td><a target="_blank" href="https://github.com/fgcneto/blockchain/raw/main/slides/02-blockchain-history.pdf"><img src="https://img.shields.io/badge/-Slides-008ED2?style=flat-square&logo=adobe-acrobat-reader"></a></td>
  </tr>
  <tr>
    <td>Leitura complementar</td>
    <td>MB Capítulo <a target="_blank" href="https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch01.asciidoc">1</a></td>
  </tr>
  <tr>
    <td>Material complementar</td>
    <td><a target="_blank" href="https://bitcoin.org/bitcoin.pdf">White paper</a> por <em>Satoshi Nakamoto</em><br><a target="_blank" href="http://www.activism.net/cypherpunk/manifesto.html">Cypherpunk Manifesto</a> por <em>E. Hughes</em><br><a target="_blank" href="https://www.blockchain.com/explorer">Blockchain Explorer</a></td>
  </tr>

  <tr>
    <td colspan="2"><strong>Arquitetura de um Blockchain: Hashing</strong></td>
  </tr>
  <tr>
    <td>Slides</td>
    <td><a target="_blank" href="https://github.com/fgcneto/blockchain/raw/main/slides/03-blockchain-architecture-hashing.pdf"><img src="https://img.shields.io/badge/-Slides-008ED2?style=flat-square&logo=adobe-acrobat-reader"></a></td>
  </tr>
  <tr>
    <td>Leitura complementar</td>
    <td>MB Capítulo <a target="_blank" href="https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch04.asciidoc">4</a></td>
  </tr>
  <tr>
    <td>Material complementar</td>
    <td><a target="_blank" href="https://andersbrownworth.com/blockchain/hash">SHA256 Online</a><br><a target="_blank" href="https://docs.python.org/3/library/hashlib.html">Documentação hashlib</a></td>
  </tr>
  
  
  <tr>
    <td colspan="2"><strong>Arquitetura de um Blockchain: Bloco</strong></td>
  </tr>
  <tr>
    <td>Slides</td>
    <td><a target="_blank" href="https://github.com/fgcneto/blockchain/raw/main/slides/04-blockchain-architecture-blocks.pdf"><img src="https://img.shields.io/badge/-Slides-008ED2?style=flat-square&logo=adobe-acrobat-reader"></a></td>
  </tr>
  <tr>
    <td>Leitura complementar</td>
    <td>MB Capítulo <a target="_blank" href="https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch09.asciidoc">9</a></td>
  </tr>
  <tr>
    <td>Material complementar</td>
    <td><a target="_blank" href="https://andersbrownworth.com/blockchain/block">Blocos: Demo</a><br><a target="_blank" href="https://andersbrownworth.com/blockchain/blockchain">Blockchain: Demo</a></td>
  </tr>
  
  <tr>
    <td colspan="2"><strong>Arquitetura de um Blockchain: Rede e Mempool</strong></td>
  </tr>
  <tr>
    <td>Slides</td>
    <td><a target="_blank" href="https://github.com/fgcneto/blockchain/raw/main/slides/05-blockchain-architecture-network-mempool.pdf"><img src="https://img.shields.io/badge/-Slides-008ED2?style=flat-square&logo=adobe-acrobat-reader"></a></td>
  </tr>
  <tr>
    <td>Leitura complementar</td>
    <td>MB Capítulo <a target="_blank" href="https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch08.asciidoc">8</a></td>
  </tr>
  <tr>
    <td>Material complementar</td>
    <td><a target="_blank" href="https://mempool.space/pt/">Bitcoin Mempool Space</a></td>
  </tr>
  
  <tr>
    <td colspan="2"><strong>Arquitetura de um Blockchain: Consenso - Proof-of-Work</strong></td>
  </tr>
  <tr>
    <td>Slides</td>
    <td><a target="_blank" href="https://github.com/fgcneto/blockchain/raw/main/slides/06-blockchain-architecture-consensus.pdf"><img src="https://img.shields.io/badge/-Slides-008ED2?style=flat-square&logo=adobe-acrobat-reader"></a></td>
  </tr>
  <tr>
    <td>Leitura complementar</td>
    <td>MB Capítulo <a target="_blank" href="https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch10.asciidoc">10</a></td>
  </tr>
  <tr>
    <td>Material complementar</td>
    <td><a target="_blank" href="https://www.mail-archive.com/cryptography@metzdowd.com/msg09997.html">E-Mail Satoshi Nakamoto: PoW</a></td>
  </tr>
  
  <tr>
    <td colspan="2"><strong>Arquitetura de um Blockchain: Consenso - Proof-of-Stake</strong></td>
  </tr>
  <tr>
    <td>Slides</td>
    <td><a target="_blank" href="https://github.com/fgcneto/blockchain/raw/main/slides/07-blockchain-architecture-consensus-advanced.pdf"><img src="https://img.shields.io/badge/-Slides-008ED2?style=flat-square&logo=adobe-acrobat-reader"></a></td>
  </tr>
  
  <tr>
    <td colspan="2"><strong>Arquitetura de um Blockchain: Assinaturas digitais</strong></td>
  </tr>
  <tr>
    <td>Slides</td>
    <td><a target="_blank" href="https://github.com/fgcneto/blockchain/raw/main/slides/08-blockchain-architecture-signatures.pdf"><img src="https://img.shields.io/badge/-Slides-008ED2?style=flat-square&logo=adobe-acrobat-reader"></a></td>
  </tr>
  <tr>
    <td>Leitura complementar</td>
    <td>MB Capítulo <a target="_blank" href="https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch04.asciidoc">4</a></td>
  </tr>
  <tr>
    <td>Material complementar</td>
    <td><a target="_blank" href="https://tools.bitcoin.com/verify-message/">Validação de assinaturas Bitcoin</a></td>
  </tr>
  <tr>
    <td colspan="2"><strong>Arquitetura de um Blockchain: Wallets </strong></td>
  </tr>
  <tr>
    <td>Slides</td>
    <td><a target="_blank" href="https://github.com/fgcneto/blockchain/raw/main/slides/09-blockchain-architecture-wallets.pdf"><img src="https://img.shields.io/badge/-Slides-008ED2?style=flat-square&logo=adobe-acrobat-reader"></a></td>
  </tr>
  <tr>
    <td>Leitura complementar</td>
    <td>MB Capítulo <a target="_blank" href="https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch05.asciidoc">5</a></td>
  </tr>
  <tr>
    <td>Material complementar</td>
    <td><a target="_blank" href="https://bitcoinpaperwallet.com/">Paper wallet</a><br><a target="_blank" href="https://bitcoin.org/en/exchanges#south-america">Bitcoin Exchanges</a><br><a target="_blank" href="https://bitcoin.org/pt_BR/escolha-sua-carteira">Escolha sua carteira (<em>wallet</em>)</a></td>
  </tr>

  <tr>
    <td colspan="2"><strong>Arquitetura de um Blockchain: Transações </strong></td>
  </tr>
  <tr>
    <td>Slides</td>
    <td><a target="_blank" href="https://github.com/fgcneto/blockchain/raw/main/slides/10-blockchain-architecture-transactions.pdf"><img src="https://img.shields.io/badge/-Slides-008ED2?style=flat-square&logo=adobe-acrobat-reader"></a></td>
  </tr>
  <tr>
    <td colspan="2"><strong>Arquitetura de um Blockchain: Script Bitcoin </strong></td>
  </tr>
  <tr>
    <td>Slides</td>
    <td><a target="_blank" href="https://github.com/fgcneto/blockchain/raw/main/slides/11-blockchain-architecture-script-bitcoin.pdf"><img src="https://img.shields.io/badge/-Slides-008ED2?style=flat-square&logo=adobe-acrobat-reader"></a></td>
  </tr>
  <tr>
    <td>Leitura complementar</td>
    <td>MB Capítulo <a target="_blank" href="https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch06.asciidoc">6</a> e <a target="_blank" href="https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch07.asciidoc">7</a></td>
  </tr>
  <tr>
    <td>Material complementar</td>
    <td><a target="_blank" href="https://en.bitcoin.it/wiki/Script">Referência da linguagem <em>Script</em></a></td>
  </tr>

  <tr>
    <td colspan="2"><strong>Arquitetura de um Blockchain: Nós e Forks </strong></td>
  </tr>
  <tr>
    <td>Slides</td>
    <td><a target="_blank" href="https://github.com/fgcneto/blockchain/raw/main/slides/12-blockchain-architecture-nodes-and-forks.pdf"><img src="https://img.shields.io/badge/-Slides-008ED2?style=flat-square&logo=adobe-acrobat-reader"></a></td>
  </tr>
    <tr>
    <td>Leitura complementar</td>
    <td>MB Capítulo <a target="_blank" href="https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch08.asciidoc">8</a> e <a target="_blank" href="https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch10.asciidoc">10</a></td>
  </tr>
  <tr>
    <td>Material complementar</td>
    <td><a target="_blank" href="https://bitcoin.org/en/download">Cliente Bitcoin Core</a></td>
  </tr>
  
  <tr>
    <td colspan="2"><strong>Ethereum e Smart Contracts </strong></td>
  </tr>
  <tr>
    <td>Slides</td>
    <td><a target="_blank" href="https://github.com/fgcneto/blockchain/raw/main/slides/13-ethereum-and-smart-contracts.pdf"><img src="https://img.shields.io/badge/-Slides-008ED2?style=flat-square&logo=adobe-acrobat-reader"></a></td>
  </tr>
    <tr>
    <td>Leitura complementar</td>
    <td>MB Capítulo <a target="_blank" href="https://github.com/ethereumbook/ethereumbook/blob/develop/07smart-contracts-solidity.asciidoc">7</a></td>
  </tr>
  <tr>
    <td>Material complementar</td>
    <td><a target="_blank" href="https://github.com/ethereumbook/ethereumbook">Mastering Ethereum</a> <em>por A. Antonopoulos</em></td>
  </tr>

  <tr>
    <td colspan="2"><strong>Ethereum - Solidity </strong></td>
  </tr>
  <tr>
    <td>Slides</td>
    <td><a target="_blank" href="https://github.com/fgcneto/blockchain/raw/main/slides/14-solidity.pdf"><img src="https://img.shields.io/badge/-Slides-008ED2?style=flat-square&logo=adobe-acrobat-reader"></a></td>
  </tr>
    <tr>
    <td>Leitura complementar</td>
    <td>MB Capítulo <a target="_blank" href="https://github.com/ethereumbook/ethereumbook/blob/develop/07smart-contracts-solidity.asciidoc">7</a></td>
  </tr>
  <tr>
    <td>Material complementar</td>
    <td><a target="_blank" href="https://docs.soliditylang.org/">Documentação Solidity</a><br><a target="_blank" href="https://cryptozombies.io//">Curso CryptoZombies</a><br><a target="_blank" href="https://remix.ethereum.org/">Remix IDE</a><br><a target="_blank" href="https://faucet.sepolia.dev/">Ether Sepolia Faucet</a></td>
  </tr>

  <tr>
    <td colspan="2"><strong>Ethereum - Tokens e NFTs </strong></td>
  </tr>
  <tr>
    <td>Slides</td>
    <td><a target="_blank" href="https://github.com/fgcneto/blockchain/raw/main/slides/15-tokens.pdf"><img src="https://img.shields.io/badge/-Slides-008ED2?style=flat-square&logo=adobe-acrobat-reader"></a></td>
  </tr>

  <tr>
    <td colspan="2"><strong>Ethereum - Dapps</strong></td>
  </tr>
    <tr>
    <td>Dapp - Lottery</td>
    <td><a target="_blank" href="https://github.com/fgcneto/blockchain/tree/main/Dapps/Lottery-Contract"></a></td>
  </tr>
  <tr>
    <td>Slides</td>
    <td><a target="_blank" href="https://github.com/fgcneto/blockchain/raw/main/slides/16-dapps.pdf"><img src="https://img.shields.io/badge/-Slides-008ED2?style=flat-square&logo=adobe-acrobat-reader"></a></td>
  </tr>
  <tr>
    <td><strong>DApp: Rifa</strong></td>
    <td><a target="_blank" href="https://github.com/fgcneto/blockchain/tree/main/Dapps/dapp-rifa"><img src="https://img.shields.io/badge/-Repositorio-181717?style=flat-square&logo=github"></a>
  </td>
  </tr> 
  <tr>
    <td><strong>DApp: Lottery</strong></td>
    <td><a target="_blank" href="https://github.com/fgcneto/blockchain/tree/main/Dapps/Lottery-Contract"><img src="https://img.shields.io/badge/-Repositorio-181717?style=flat-square&logo=github"></a></td>
  </tr>
  <tr>
    <td>Leitura complementar</td>
    <td>MB Capítulo <a target="_blank" href="https://github.com/ethereumbook/ethereumbook/blob/develop/10tokens.asciidoc">10</a> e <a target="_blank" href="https://github.com/ethereumbook/ethereumbook/blob/develop/12dapps.asciidoc">12</a></td>
  </tr>
  <tr>
    <td>Material complementar</td>
    <td><a target="_blank" href="https://docs.soliditylang.org/">Documentação Solidity</a><br><a target="_blank" href="https://remix.ethereum.org/">Remix IDE</a></td>
  
    
</table>

## Projetos

```markdown
.
├── blockchain-python
│   ├── 01-hashing
│   │   └── blockchain.py
| ├── 02-blocks
|   │   └── blockchain.py
| ├── 03-pow
|   │   └── blockchain.py
| ├── 04-sign-and-verify
|   │   └── blockchain.py
| ├── 05-transactions
|   │   └── blockchain.py
| ├── 06-consensus
|   │   └── blockchain.py
└── final-project
└── [...]
```

## Licença

[MIT](https://choosealicense.com/licenses/mit/)
