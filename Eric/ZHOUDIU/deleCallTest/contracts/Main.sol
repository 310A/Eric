pragma solidity ^0.4.6;

contract Main { 
    mapping(bytes4=>uint32) public returnSizes; 
    uint8 public z; 
    address public upgradeContract; 
    address public dispatcherContract; 
    
    // function deployDispatcher() returns (address) { 
    //     dispatcherContract = new Dispatcher(); 
    //     return dispatcherContract;
    // } 
    
    function getValue() returns (uint32) {
        return returnSizes[bytes4(sha3("get()"))];
    }
    
    function setDispatcherContract(address a) {
        dispatcherContract = a;
    }
    
    function updateUpgrade(address newUpgradeContract) { 
        dispatcherContract.delegatecall( 
            bytes4 ( sha3("replace(address)")), newUpgradeContract 
        ); 
    } 
    
    function delegateCall(bytes4 _sig, uint8 _x, uint8 _y) { 
        dispatcherContract.delegatecall(_sig, _x, _y); 
    }
    
    function get() constant returns(int output ) {
        dispatcherContract.delegatecall(bytes4( sha3("get()"))); 
        assembly { 
            // log0(0x0,128)
            output := mload(0x60) 
        } 
    }
    
    function convert(uint256 n) returns (bytes32) {
      return bytes32(n);
    }

}

