pragma solidity ^0.8.17;

contract Rifa {
    address payable owner;
    mapping(address => uint256) rifasPorPessoa;
    address[] players;
    uint256 valorDaRifa = 0.1 ether;
    address payable winner;
    uint256 prize = 0;

    event Sorteio(address winner);
    event RifaComprada(address comprador, uint256 quant);

    constructor() public {
        // Recebe Endereco de quem realizou o deploy
        owner = msg.sender;
    }

    function random() private view returns (uint256) {
        return uint256(keccak256(block.difficulty, now, players));
    }

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }

    function sacarPremio() external onlyOwner {
        winner.transfer(this.balance);
    }

    function verRifas() public view returns (uint256);

    function comprarRifa(uint256 _quant) public payable {
        require(msg.value > 0.01 ether);
        players.push(msg.sender);
    }

    function sortearRifa() public onlyOwner {
        uint256 index = random() % players.length;
        winner = players[index];
    }

    function verPremio() public view returns (uint256) {
        this.balance;
    }

    function verTotalDeRifas() public view returns (uint256) {
        return players.length;
    }

    function verGanhador() public view returns (address) {
        return winner;
    }

    function verPrecoDaRifa() public view returns (uint256) {
        return valorDaRifa;
    }

    function isOwner() public view returns (bool) {
        if (msg.sender == owner) {
            return true;
        } else {
            return false;
        }
    }
}
