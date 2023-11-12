from tether import Tether
from configparser import ConfigParser

class AutomatedWallet:
    def __init__(self, config_file):
        self.config = ConfigParser()
        self.config.read(config_file)
        self.tether = Tether()

    def get_balance(self):
        return self.tether.get_balance(self.config['Wallet']['public_key'])

    def send_transaction(self, to_address, amount):
        before_balance = self.get_balance()
        transaction_result = self.tether.send_transaction(
            self.config['Wallet']['private_key'], to_address, amount
        )
        after_balance = self.get_balance()

        print(f"Before Transaction Balance: {before_balance}")
        print(f"After Transaction Balance: {after_balance}")

        return transaction_result

if __name__ == "__main__":
    config_file = "config.ini"
    wallet = AutomatedWallet(config_file)

    # Example: Send 10 USDT to another address
    to_address = "RECIPIENT_ADDRESS"
    amount = 10

    transaction_result = wallet.send_transaction(to_address, amount)
    print(f"Transaction Result: {transaction_result}")

