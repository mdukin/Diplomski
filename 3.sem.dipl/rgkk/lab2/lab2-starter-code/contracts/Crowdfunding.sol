// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./Timer.sol";

/// This contract represents most simple crowdfunding campaign.
/// This contract does not protects investors from not receiving goods
/// they were promised from crowdfunding owner. This kind of contract
/// might be suitable for campaigns that does not promise anything to the
/// investors except that they will start working on some project.
/// (e.g. almost all blockchain spinoffs.)
contract Crowdfunding {

    address private owner;

    Timer private timer;

    uint256 public goal;

    uint256 public endTimestamp;

    mapping (address => uint256) public investments;

    bool claimed ;
    constructor(
        address _owner,
        Timer _timer,
        uint256 _goal,
        uint256 _endTimestamp
    ) {
        owner = (_owner == address(0) ? msg.sender : _owner);
        timer = _timer; // Not checking if this is correctly injected.
        goal = _goal;
        endTimestamp = _endTimestamp;
        claimed = false;
    }

    function invest() public payable {
        // TODO Your code here
        require(timer.getTime() < endTimestamp, "Crowdfunding has ended.");
        require(msg.value > 0, "Investment must be greater than 0.");

        investments[msg.sender] += msg.value;
        if(owner !=msg.sender)
            investments[owner] += msg.value;
    }

    function claimFunds() public {
        // TODO Your code here
        require(claimed == false, "funds already claimed.");
        require(msg.sender == owner, "Only the owner can claim funds.");
        require(timer.getTime() >= endTimestamp, "Crowdfunding is still ongoing.");
    
        require(investments[owner] >= goal, "Goal not reached, cannot claim funds.");
        
        (bool success, ) = owner.call{value: investments[owner]}("");
        require(success, "Claim funds failed.");
        claimed = true;
    }

    function refund() public {
        // TODO Your code here
        require(timer.getTime() >= endTimestamp, "Crowdfunding is still ongoing.");
        require(investments[owner] < goal , "Goal was reached, no refunds available.");

        require(investments[msg.sender] > 0, "You have no investments to refund.");

        (bool success, ) = msg.sender.call{value: investments[msg.sender]}("");
        require(success, "Refund failed.");
        investments[msg.sender] = 0; 
    }
    
}