from web3 import Web3
import json

class PolygonWallet:
    def __init__(self, config_file):
        self.web3 = Web3(Web3.HTTPProvider('https://rpc-mainnet.matic.network'))
        self.load_config(config_file)

    def load_config(self, config_file):
        with open(config_file, 'r') as file:
            config = json.load(file)
            self.address = config['address']
            self.private_key = config['private_key']

    def get_balance(self):
        balance = self.web3.eth.getBalance(self.address)
        return self.web3.fromWei(balance, 'ether')

    def send_transaction(self, to_address, value):
        value_wei = self.web3.toWei(value, 'ether')
        transaction = {
            'to': to_address,
            'value': value_wei,
            'gas': 21000,
            'gasPrice': self.web3.toWei('5', 'gwei'),
            'nonce': self.web3.eth.getTransactionCount(self.address),
        }
        signed_transaction = self.web3.eth.account.signTransaction(transaction, self.private_key)
        transaction_hash = self.web3.eth.sendRawTransaction(signed_transaction.rawTransaction)
        return transaction_hash

    def display_balance(self):
        balance_before = self.get_balance()
        print(f"Before transaction balance: {balance_before} ETH")

    def execute_transaction(self, to_address, value):
        self.display_balance()
        transaction_hash = self.send_transaction(to_address, value)
        print(f"Transaction Hash: {transaction_hash}")
        balance_after = self.get_balance()
        print(f"After transaction balance: {balance_after} ETH")

if __name__ == "__main__":
    config_file = 'config.json'  # Update with your configuration file path
    wallet = PolygonWallet(config_file)

    # Example: Send 0.1 ETH to another address
    to_address = '0xYourRecipientAddress'
    value = 0.1

    wallet.execute_transaction(to_address, value)

