# delecateCallTest
Using delecatecall() to call functions in other contracts and get its return value
ps. Only Dispather.sol and Upgrade.sol are used in run.js.

# Installation
npm install

# Run
node run.js

# Usage
run.js will compile and deploy Register.sol to http://localhost:8545 automatically if it wasn't deployed before, then call Dispatcher.sol's add() and get its return value.