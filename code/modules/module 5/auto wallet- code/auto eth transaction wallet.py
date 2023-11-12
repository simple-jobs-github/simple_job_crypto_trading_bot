from web3 import Web3

class EthereumWallet:
    def __init__(self, config_file_path):
        self.web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_API_KEY'))  # Replace with your Infura API key
        self.config_file_path = config_file_path
        self.load_config()

    def load_config(self):
        with open(self.config_file_path, 'r') as file:
            lines = file.readlines()
            self.address = lines[0].strip()
            self.private_key = lines[1].strip()

    def get_balance(self):
        balance = self.web3.eth.getBalance(self.address)
        return self.web3.fromWei(balance, 'ether')

    def display_balance(self, message):
        print(f"{message} Balance: {self.get_balance()} ETH")

    def send_transaction(self, to_address, value):
        nonce = self.web3.eth.getTransactionCount(self.address)
        gas_price = self.web3.eth.gas_price

        transaction = {
            'to': to_address,
            'value': self.web3.toWei(value, 'ether'),
            'gas': 21000,
            'gasPrice': gas_price,
            'nonce': nonce,
        }

        signed_transaction = self.web3.eth.account.sign_transaction(transaction, self.private_key)
        transaction_hash = self.web3.eth.sendRawTransaction(signed_transaction.rawTransaction)
        return transaction_hash.hex()

if __name__ == "__main__":
    wallet = EthereumWallet('config.txt')  # Replace with your configuration file path

    # Display initial balance
    wallet.display_balance("Before Transaction")

    # Example: Sending 0.1 ETH to another address
    to_address = '0xReceiverAddress'  # Replace with the recipient's Ethereum address
    value_to_send = 0.1

    # Sending the transaction
    transaction_hash = wallet.send_transaction(to_address, value_to_send)
    print(f"Transaction Hash: {transaction_hash}")

    # Display updated balance
    wallet.display_balance("After Transaction")

