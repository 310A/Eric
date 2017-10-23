pragma solidity ^0.4.11;

contract Plus {
    int z;
    string s;
    function plus(int x, int y) { //sig:"0xccf65503"
        z = x+y;
    }
    function plus2(string a) {
        s = a;
    }
}