// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./Auction.sol";

contract EnglishAuction is Auction {

    uint internal highestBid;
    uint internal initialPrice;
    uint internal biddingPeriod;
    uint internal lastBidTimestamp;
    uint internal minimumPriceIncrement;

    address internal highestBidder = address(0);

    constructor(
        address _sellerAddress,
        address _judgeAddress,
        Timer _timer,
        uint _initialPrice,
        uint _biddingPeriod,
        uint _minimumPriceIncrement
    ) Auction(_sellerAddress, _judgeAddress, _timer) {
        initialPrice = _initialPrice;
        biddingPeriod = _biddingPeriod;
        minimumPriceIncrement = _minimumPriceIncrement;

        // Start the auction at contract creation.
        lastBidTimestamp = time();
    }

    function bid() public payable {
        // TODO Your code here
        require(lastBidTimestamp + biddingPeriod > time() );
        require(msg.value>=initialPrice );
        require(msg.value-highestBid >= minimumPriceIncrement);

        if (highestBidder != address(0)) {
            (bool success, ) = highestBidder.call{value: highestBid}("");
            require(success, "failed.");
        }


        highestBid = msg.value;
        highestBidder = msg.sender;
        lastBidTimestamp = time();
        
    }

    function getHighestBidder() override public returns (address) {
        // TODO Your code here
       if(highestBidder == address(0) || time()<lastBidTimestamp+biddingPeriod) 
            return address(0);

        outcome = Outcome.SUCCESSFUL;
        return highestBidder;

    }

    function enableRefunds() public {
        // TODO Your code here
        require(lastBidTimestamp + biddingPeriod < time() );
        require(highestBidder == address(0));
        outcome = Outcome.NOT_SUCCESSFUL;
    }

}