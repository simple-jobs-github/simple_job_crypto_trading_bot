from avaxpython import avax
import configparser

def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['wallet']['public_key'], config['wallet']['private_key']

def get_balance(public_key):
    # Implement a function to get the balance from the blockchain
    # You may use avax-python functions for this

def send_transaction(sender_private_key, receiver_address, amount):
    # Implement a function to send a transaction using avax-python

if __name__ == '__main__':
    # Read configuration
    public_key, private_key = read_config()

    # Display current cryptocurrency
    print("Current cryptocurrency: AVAX")

    # Display before transaction balance
    before_balance = get_balance(public_key)
    print(f"Before transaction balance: {before_balance}")

    # Perform transaction
    receiver_address = "RECEIVER_ADDRESS"
    amount_to_send = 10  # Adjust the amount as needed
    send_transaction(private_key, receiver_address, amount_to_send)

    # Display after transaction balance
    after_balance = get_balance(public_key)
    print(f"After transaction balance: {after_balance}")

