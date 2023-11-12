from bitcoinlib.wallets import Wallet, wallet_create_or_open
from bitcoinlib.transactions import Transaction

class AutomatedBitcoinWallet:
    def __init__(self, config_file_path):
        self.wallet = wallet_create_or_open(config_file=config_file_path)
        self.currency = self.wallet.currency()
        self.balance_before_transaction = None
        self.balance_after_transaction = None

    def get_balance(self):
        return self.wallet.balance()

    def display_balance(self, message):
        balance = self.get_balance()
        print(f"{message} Balance: {balance} {self.currency}")

    def create_transaction(self, to_address, amount):
        self.balance_before_transaction = self.get_balance()
        
        tx = Transaction.create('payment', [({'address': to_address}, amount)])
        tx_signed = self.wallet.sign_transaction(tx)
        tx_broadcasted = tx_signed.send()
        
        self.balance_after_transaction = self.get_balance()
        return tx_broadcasted

if __name__ == "__main__":
    config_file_path = "path/to/your/config/file.conf"
    wallet = AutomatedBitcoinWallet(config_file_path)

    # Display initial balance
    wallet.display_balance("Before Transaction")

    # Example: Send Bitcoin to another address
    to_address = "destination_address"
    amount_to_send = 0.001  # Specify the amount to send

    # Create and broadcast the transaction
    tx_result = wallet.create_transaction(to_address, amount_to_send)

    # Display final balance
    wallet.display_balance("After Transaction")

    print("Transaction Result:", tx_result)
