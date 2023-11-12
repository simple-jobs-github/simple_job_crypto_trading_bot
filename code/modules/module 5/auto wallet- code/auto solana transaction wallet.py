from solana.account import Account
from solana.rpc.api import Client
from solana.transaction import Transaction, TransactionInstruction, SYS_PROGRAM_ID
from solana.system_program import TransferParams

class SolanaWallet:
    def __init__(self, config_file):
        self.config = self.read_config(config_file)
        self.account = Account(bytes.fromhex(self.config['private_key']))
        self.client = Client(self.config['rpc_url'])

    def read_config(self, config_file):
        # Read configuration from the file
        # Example config file:
        # private_key = "your_private_key"
        # rpc_url = "https://api.devnet.solana.com"
        with open(config_file, 'r') as file:
            config = dict(line.strip().split('=') for line in file)
        return config

    def get_balance(self):
        # Get balance of the wallet
        balance = self.client.get_balance(self.account.public_key())
        return balance

    def display_balance(self, message):
        # Display balance with a custom message
        print(f"{message}: {self.get_balance()} SOL")

    def send_transaction(self, to_address, amount):
        # Create a transaction
        transaction = Transaction(recent_blockhash=self.client.get_recent_blockhash())
        transaction.add(TransferParams(from_pubkey=self.account.public_key(),
                                      to_pubkey=to_address,
                                      lamports=amount))

        # Sign the transaction
        transaction.sign(self.account)

        # Send the transaction
        result = self.client.send_transaction(transaction)

        # Display before and after transaction balances
        self.display_balance("Before transaction balance")
        self.display_balance("After transaction balance")

        return result

if __name__ == "__main__":
    # Example usage
    config_file = "path/to/your/config.txt"
    wallet = SolanaWallet(config_file)

    # Display initial balance
    wallet.display_balance("Initial balance")

    # Example: Sending 1 SOL to another address
    to_address = "destination_address"
    amount = 1_000_000_000  # Amount in lamports (1 SOL = 1,000,000,000 lamports)
    result = wallet.send_transaction(to_address, amount)

    print(f"Transaction ID: {result['result']}")

