pragma solidity ^0.4.11;

contract Dispatcher { 
    mapping(bytes4=>uint32) public returnSizes; 
    uint256 public z; 
    address upgradeContract; 

    function Dispatcher() {
        // z = 2;
    }

    function replace(address newUpgradeContract) { 
        upgradeContract = newUpgradeContract; 
        upgradeContract.delegatecall(bytes4(sha3("initialize()"))); 
    }
    function getValue() returns (uint32) {
        return returnSizes[bytes4(sha3("plus(uint256,uint256)"))];
    }

    function setZ(uint256 _x) returns (uint256) {
        bytes4 _sig = bytes4(keccak256("test(uint256)")); 
        //0xf8a8fd6d
        var target = upgradeContract; 
        // upgradeContract.delegatecall(bytes4(sha3("test(uint)")))
        assembly {
            mstore(0x0, _sig)
            // log0(0x0, 4)
            mstore(0x4, _x)
            let a:= delegatecall(3000000, target, 0x0, 36, 0x0, 32)
            log1(0x0, 32, "weige")
            // return(0x0, 32)
        }

    }

    function add(uint256 _x, uint256 _y) returns (uint256) { 
        var len = 32;
        bytes4 _sig = bytes4(keccak256("plus(uint256,uint256)"));
        // returnSizes[sig];
        var target = upgradeContract; 
        //"0x916f4029",2,3
        assembly { 
            mstore(0x0, _sig)
            log1(0x0, 32, "wei1")
            calldatacopy(0x4, 0x4, calldatasize) 
            log1(0x0, calldatasize, "wei2")
            let a:= delegatecall(3000000, target, 0x0, calldatasize, 0x40, len) 
            log1(0x40, 32, "weige")
            return(0x40, len) 
        }
    } 
}