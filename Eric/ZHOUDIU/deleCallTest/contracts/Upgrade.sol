pragma solidity ^0.4.11;

contract Upgrade { 
    mapping(bytes4=>uint32) returnSizes; 
    uint256 z; 
    function getValue() returns (uint32) {
        return returnSizes[bytes4(sha3("get()"))];
    }
    function initialize() { 
        returnSizes[bytes4(sha3("plus(uint256,uint256)"))] = 32; 
    } 
    
    function plus(uint256 _x,uint256 _y) returns (uint256) { 
        z = _x + _y; 
        return z;
    } 
    
    function get() returns(uint256) { 
        return z; 
    } 

    function test(uint256 _x) returns (uint256) {
        z = _x;
        return z;
    }
}