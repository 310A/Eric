// const Register = require('./register');
const CompileDeploy = require('./compile_deploy')
const Web3 = require('web3')
const fs = require('fs')
const config  = require('./config.json')


const {endpoint, account, cost} = config;

async function run() {

    let disAddress = "";
    let upgradeAddress = "";
    const path1 = './build/DispatcherContractAddress.txt';
    const path2 = './build/UpgradeContractAddress.txt';

    if(fs.existsSync(path1) && fs.existsSync(path2)) {
        disAddress = fs.readFileSync(path1);
        upgradeAddress = fs.readFileSync(path2);
    }

    if(disAddress == "" || upgradeAddress == "") {
        console.log("Deploy contracts now...");
        await CompileDeploy("Upgrade");
        await CompileDeploy("Dispatcher");
        disAddress = fs.readFileSync(path1);
        upgradeAddress = fs.readFileSync(path2);
    }

    console.log("disAddress: " + disAddress);
    console.log("upgradeAddress: " + upgradeAddress);

    const web3 =  new Web3(new Web3.providers.HttpProvider(endpoint));
    web3.personal.unlockAccount(account.address, account.password);

    disAbi = fs.readFileSync('./build/Dispatcher.abi');

    const disContract = web3.eth.contract(JSON.parse(disAbi));
    const disToken = disContract.at(disAddress.toString());
    // console.log(disToken.getZ.call().toString());

    await disToken.replace.sendTransaction(upgradeAddress.toString(), {from: "0x3ae88fe370c39384fc16da2c9e768cf5d2495b48", gas: 3000000});
    let result = 0;

    //过滤log1 "weige"的事件
    let hex = '0x' + Buffer.from("weige", 'utf8').toString("hex");
    for(let i = hex.length; i < 66; i++) {
        hex += '0';
    }
    const filter = web3.eth.filter({topics: [hex]});
    filter.watch(function (error, log) {
        //得到setZ()内存0x0到32位置的值
        console.log(log.data);
        result = parseInt(log.data); 
        console.log("result: " + result);  
        filter.stopWatching();      
      });
    
    await disToken.add(3, 4, {from: "0x3ae88fe370c39384fc16da2c9e768cf5d2495b48", gas: 4000000}, (err, res) => {
        // console.log(res);
    });
    // console.log(disToken.getZ.call().toString());
    // filter.stopWatching();
}

run()

