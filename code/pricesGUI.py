import tkinter as tk
from tkinter import ttk
import requests

class CryptoPriceCheckerApp:
    def __init__(self, master):
        self.master = master
        master.title("Crypto Price Checker")

        # Create and configure widgets
        self.crypto_label = tk.Label(master, text="Select Cryptocurrency:")
        self.crypto_combobox = ttk.Combobox(master, values=['Bitcoin', 'Ethereum', 'Litecoin', 'BNB', 'Tether', 'XRP', 'USDC',
                                                            'Solana', 'Lido Staked Ether', 'Cardano', 'Dogecoin', 'TRON', 'Polygon',
                                                            'Chainlink', 'Dai', 'Monero', 'NEO', ' Celestia'])  # Add more cryptocurrencies as needed
        self.fetch_button = tk.Button(master, text="Fetch Price", command=self.fetch_price)
        self.result_label = tk.Label(master, text="")

        # Place widgets in the window
        self.crypto_label.grid(row=0, column=0, padx=10, pady=10)
        self.crypto_combobox.grid(row=0, column=1, padx=10, pady=10)
        self.fetch_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)

    def get_crypto_prices(self, crypto_id, vs_currency='usd'):
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={vs_currency}"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad responses (4xx and 5xx)
            data = response.json()
            price = data[crypto_id][vs_currency]
            return price
        except requests.exceptions.RequestException as e:
            print(f"Error fetching cryptocurrency price: {e}")
            return None

    def fetch_price(self):
        selected_crypto = self.crypto_combobox.get()
        if selected_crypto:
            price = self.get_crypto_prices(selected_crypto.lower())
            if price is not None:
                self.result_label.config(text=f"Current {selected_crypto.capitalize()} price: ${price}")
            else:
                self.result_label.config(text="Failed to fetch cryptocurrency price.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoPriceCheckerApp(root)
    root.mainloop()
