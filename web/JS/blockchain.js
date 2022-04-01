const SHA256 = require('crypto-js/sha256')// npm install --save crypto-js

class Transaction{
    constructor(fromAddress,toAddress, amount){
        this.fromAddress = fromAddress;
        this.toAddress = toAddress;
        this.amount = amount;
    }
}
class Block{
    constructor(timestamp,data,previousHash=''){
        this.timestamp = timestamp;
        this.data = data;
        this.previousHash = previousHash;
        this.hash = this.calculateHash();
        this.nonce = 0;
    }
    calculateHash(){
        return SHA256(this.timestamp + this.previousHash + JSON.stringify(this.data) + this.nonce).toString();
    }
    /* Proof-of-Work, or PoW, is the original consensus algorithm in a Blockchain network.
       this algorithm is used to confirm transactions and produce new blocks to the chain. 
       With PoW, miners compete against each other to complete transactions on the network and get rewarded. 
       and make sure that one block is created every 10mn*/
    mineBlock(difficulty){
        while(this.hash.substring(0,difficulty) != Array(difficulty +1).join("0")){
            this.nonce++;
            this.hash = this.calculateHash();
        }
    }
}
class Blockchain{
    constructor(){
        this.chain = [this.createGenesisBlock()];
        this.difficulty = 2;
        this.pendingTransactions = [];
        this.miningReward = 100;
    }
    // first Block in the Blochchain
    createGenesisBlock(timestamp="01/01/2022",previousHash="0"){
        return new Block(timestamp,previousHash);
    }

    getLatesBlock(){
        return this.chain[this.chain.length - 1];
    }

    minePendingTransactions(miningRewardAddress){
        let block = new Block(Data.now(),this.pendingTransactions);
        block.mineBlock(this.difficulty);

        console.log('Block Succeddfully mined!');
        this.chain.push(block);

        this.pendingTransactions = [
            new Transaction(null,miningRewardAddress,this.miningReward)
        ];
    }

    createTransaction(transaction){
        this.pendingTransactions.push(transaction);
    }

    getBalanceOfAddress(address){
        let balance = 0;

        for (const block of this.chain){
            for(const trans of block.transactions){
                if(trans.fromAddress ===address){
                    balance -= trans.amount;
                }
                if (trans.toAddress ===address){
                    balance += trans.amount;
                }
            }
        }
        return balance;
    }
    // verifie is the chain is valild or not if u add a block to the chain
    isChainValid(){
        for(let i=1; i<this.chain.length; i++){
            const currentBlock = this.chain[i];
            const previousBlock = this.chain[i-1];
            if(currentBlock.hash != currentBlock.calculateHash()){//verifie if hash is the same as le new hash
                return false;
            }
            if(currentBlock.previousHash != previousBlock.hash){ //vérifie if the previous Block have the last hash
                return false;
            }
        }
        return true;
    }
}

let savjeeCoin = new Blockchain();
savjeeCoin.createTransaction(new Block('address1','address2', 10));
savjeeCoin.createTransaction(new Block('address2','address3', 41));
savjeeCoin.createTransaction(new Block('address2','address1', 40));

console.log(JSON.stringify(savjeeCoin,null,4));
savjeeCoin.minePendingTransactions('xaviers-address');

console.log('\nBalance of xavier is', savjeeCoin.getBalanceOfAddress('xaviers-address'));

