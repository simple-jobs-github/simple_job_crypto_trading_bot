import configparser
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

class LitecoinWallet:
    def __init__(self, config_file_path='wallet_config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file_path)

        self.rpc_connection = AuthServiceProxy(
            f"http://{self.config['rpc']['username']}:{self.config['rpc']['password']}@{self.config['rpc']['host']}:{self.config['rpc']['port']}"
        )

    def get_balance(self):
        return self.rpc_connection.getbalance()

    def send_transaction(self, to_address, amount):
        before_balance = self.get_balance()

        try:
            txid = self.rpc_connection.sendtoaddress(to_address, amount)
            print(f"Transaction ID: {txid}")
        except JSONRPCException as e:
            print(f"Error: {e}")

        after_balance = self.get_balance()

        print(f"Before Transaction Balance: {before_balance}")
        print(f"After Transaction Balance: {after_balance}")

if __name__ == "__main__":
    wallet = LitecoinWallet()

    # Example: Send 0.1 LTC to a specific address
    to_address = "your_destination_address"
    amount = 0.1

    wallet.send_transaction(to_address, amount)

