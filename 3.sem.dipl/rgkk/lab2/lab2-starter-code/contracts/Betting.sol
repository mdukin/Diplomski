// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./BoxOracle.sol";

contract Betting {

    struct Player {
        uint8 id;
        string name;
        uint totalBetAmount;
        uint currCoef; 
    }
    struct Bet {
        address bettor;
        uint amount;
        uint player_id;
        uint betCoef;
    }

    address private betMaker;
    BoxOracle public oracle;
    uint public minBetAmount;
    uint public maxBetAmount;
    uint public totalBetAmount;
    uint public thresholdAmount;

    Bet[] private bets;
    Player public player_1;
    Player public player_2;

    uint wonInput = 0;
    bool private suspended = false;
    mapping (address => uint) public balances;
    
    constructor(
        address _betMaker,
        string memory _player_1,
        string memory _player_2,
        uint _minBetAmount,
        uint _maxBetAmount,
        uint _thresholdAmount,
        BoxOracle _oracle
    ) {
        betMaker = (_betMaker == address(0) ? msg.sender : _betMaker);
        player_1 = Player(1, _player_1, 0, 200);
        player_2 = Player(2, _player_2, 0, 200);
        minBetAmount = _minBetAmount;
        maxBetAmount = _maxBetAmount;
        thresholdAmount = _thresholdAmount;
        oracle = _oracle;

        totalBetAmount = 0;
    }

    receive() external payable {}

    fallback() external payable {}
    
    function makeBet(uint8 _playerId) public payable {
        //TODO Your code here
        require(msg.sender != betMaker, "Owner can't bet.");
        require(!suspended, "Betting is currently suspended.");
        require(oracle.getWinner() == 0, "Match has ended.");
        require(msg.value >= minBetAmount, "Bet amount is below the minimum.");
        require(msg.value <= maxBetAmount, "Bet amount exceeds the maximum.");
        require(_playerId == player_1.id || _playerId == player_2.id, "Invalid player ID.");
        
        balances[msg.sender] +=msg.value;

        uint betCoef;

        if (_playerId == player_1.id) {
            betCoef = player_1.currCoef;
            player_1.totalBetAmount += msg.value;
        } else if (_playerId == player_2.id) {
            betCoef = player_2.currCoef;
            player_2.totalBetAmount += msg.value;
        }

        Bet memory newBet = Bet({
            bettor: msg.sender,
            amount: msg.value,
            player_id: _playerId,
            betCoef: betCoef
        });

        bets.push(newBet) ;

        totalBetAmount += msg.value;

        if(totalBetAmount > thresholdAmount){
            if(player_1.totalBetAmount % totalBetAmount == 0){
                suspended = true;
            }
            else{
                player_1.currCoef = (100 * totalBetAmount)/player_1.totalBetAmount;
                player_2.currCoef =(100 * totalBetAmount)/player_2.totalBetAmount;
            }
        }

    }

    function claimSuspendedBets() public  {
        //TODO Your code here
        require(suspended, "Betting is not suspended.");
        require(balances[msg.sender] > 0, "You have no investments to refund.");

        (bool success, ) = msg.sender.call{value: balances[msg.sender]}("");
        require(success, "Refund failed.");
        balances[msg.sender] = 0; 
    }

    function claimWinningBets() public {
        require(oracle.getWinner() != 0, "Match hasn't ended.");
        require(!suspended, "Betting is currently suspended.");

        require(balances[msg.sender] > 0, "You didn't bet or u already claimed.");

        uint wonAmount = 0;

        for (uint i = 0; i < bets.length; i++) {
            if (bets[i].bettor == msg.sender && bets[i].player_id == oracle.getWinner() ) {
                wonInput += bets[i].amount;
                wonAmount += (bets[i].amount * bets[i].betCoef) / 100;
            }
        }
        if(wonAmount > 0){
            (bool success, ) = msg.sender.call{value: wonAmount }("");
            require(success, "claim failed.");
        }
        balances[msg.sender] = 0;
    }

    function claimLosingBets() public {
        // TODO Your code here
        require(msg.sender == betMaker, "Only owner.");
        require(oracle.getWinner() != 0, "Match hasn't ended.");

        uint lostAmount = 0;
        uint wonInput = 0;
        for (uint i = 0; i < bets.length; i++) {
            if (bets[i].player_id != oracle.getWinner() ){
                lostAmount += bets[i].amount ;
            } 
        }

        require(lostAmount +wonInput == totalBetAmount, "Everyone didn't claim");
        (bool success, ) = msg.sender.call{value: lostAmount }("");
        require(success, "claim failed.");
    }
}