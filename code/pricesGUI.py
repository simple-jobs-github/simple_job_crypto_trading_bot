import tkinter as tk
from tkinter import ttk
import requests

def get_crypto_prices(crypto_id, vs_currency='usd'):
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

def fetch_price():
    selected_crypto = crypto_combobox.get()
    if selected_crypto:
        price = get_crypto_prices(selected_crypto.lower())
        if price is not None:
            result_label.config(text=f"Current {selected_crypto.capitalize()} price: ${price}")
        else:
            result_label.config(text="Failed to fetch cryptocurrency price.")

# Create main window
root = tk.Tk()
root.title("Crypto Price Checker")

# Create and configure widgets
crypto_label = tk.Label(root, text="Select Cryptocurrency:")
crypto_combobox = ttk.Combobox(root, values=['Bitcoin', 'Ethereum', 'Litecoin'])  # Add more cryptocurrencies as needed
fetch_button = tk.Button(root, text="Fetch Price", command=fetch_price)
result_label = tk.Label(root, text="")

# Place widgets in the window
crypto_label.grid(row=0, column=0, padx=10, pady=10)
crypto_combobox.grid(row=0, column=1, padx=10, pady=10)
fetch_button.grid(row=1, column=0, columnspan=2, pady=10)
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
