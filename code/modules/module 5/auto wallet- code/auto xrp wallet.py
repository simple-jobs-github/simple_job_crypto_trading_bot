# Install xrpl-py using: pip install xrpl
from xrpl.wallet import Wallet, XRPLWallet

class XRPAutomatedWallet:
    def __init__(self, config_file_path):
        self.wallet = self.load_wallet_from_config(config_file_path)

    def load_wallet_from_config(self, config_file_path):
        # Load public and private keys from the configuration file
        with open(config_file_path, 'r') as file:
            lines = file.readlines()
            public_key = lines[0].strip()
            private_key = lines[1].strip()

        return Wallet(public_key, private_key)

    def display_balance(self):
        # Fetch and display the current balance
        balance = self.wallet.get_balance()
        print(f"Current balance: {balance} XRP")

    def send_transaction(self, destination_address, amount):
        # Display the balance before the transaction
        self.display_balance()

        # Build and sign the transaction
        transaction = self.wallet.send_xrp(destination_address, amount)
        signed_transaction = XRPLWallet.sign_transaction(transaction, self.wallet.private_key)

        # Submit the transaction to the XRP Ledger
        response = XRPLWallet.submit_transaction(signed_transaction)

        # Display the balance after the transaction
        self.display_balance()

        return response

# Example Usage:
config_file_path = 'path/to/your/config/file.txt'
wallet = XRPAutomatedWallet(config_file_path)

# Example: Display current balance
wallet.display_balance()

# Example: Send XRP to another address
destination_address = 'rHb9CJAWyB4rj91VRWn96DkukG4bwdtyTh'
amount = '10'  # Amount of XRP to send
response = wallet.send_transaction(destination_address, amount)

# Print the transaction response
print("Transaction Response:", response)

