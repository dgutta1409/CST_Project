import tkinter as tk
from tkinter import ttk, messagebox
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from threading import Thread

# Fetch Crypto Data from CoinGecko API (No API Key Required)
def fetch_crypto_data(coin):
    url = f"https://api.coingecko.com/api/v3/coins/{coin}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Unable to fetch cryptocurrency data: {e}")
        return None

# Display Cryptocurrency Data in GUI
def display_crypto_data():
    coin = crypto_combobox.get().lower().replace(" ", "-")
    if not coin:
        messagebox.showwarning("Input Error", "Please select a cryptocurrency.")
        return
    result_label.config(text="Fetching crypto data...")
    Thread(target=lambda: update_crypto_data(fetch_crypto_data(coin))).start()

# Update Cryptocurrency Data on GUI
def update_crypto_data(data):
    if data:
        price = data['market_data']['current_price']['usd']
        change = data['market_data']['price_change_percentage_24h']
        crypto_info = f"{data['name']}:\nPrice: ${price:.2f}\n24h Change: {change:.2f}%"
        result_label.config(text=crypto_info)

# Stock Data (Static for Demonstration)
stock_data = {
    'stock_symbol': ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA'],
    'closing_price': [150, 2800, 300, 3400, 700],
    'change_percentage': [1.5, 0.5, 2.0, -0.5, 3.2]
}
df_stock = pd.DataFrame(stock_data)

# Display Stock Data in GUI
def display_stock_data():
    selected_stock = stock_combobox.get()
    if not selected_stock:
        messagebox.showwarning("Input Error", "Please select a stock symbol.")
        return

    # Find the selected stock's data
    stock_info = df_stock[df_stock['stock_symbol'] == selected_stock]
    price = stock_info['closing_price'].values[0]
    change = stock_info['change_percentage'].values[0]

    stock_info_str = f"Stock Symbol: {selected_stock}\nClosing Price: ${price:.2f}\nChange: {change:.2f}%"
    result_label.config(text=stock_info_str)

# Perform Analysis on Data and Plot Results
def analyze_and_plot_data():
    data = {
        'Parameter': ['Apple', 'Google', 'Microsoft', 'Amazon', 'Tesla'],
        'Value': [150, 2800, 300, 3400, 700]
    }
    df = pd.DataFrame(data)

    plt.figure(figsize=(6, 4))
    sns.barplot(x='Parameter', y='Value', data=df)
    plt.title('Stock Data Analysis')
    plt.show()

# GUI Setup
root = tk.Tk()
root.title("Custom Intelligent Application")
root.geometry("600x400")

tab_control = ttk.Notebook(root)

# Tab 1: Cryptocurrency Data
crypto_tab = ttk.Frame(tab_control)
tab_control.add(crypto_tab, text='Cryptocurrency Data')

tk.Label(crypto_tab, text="Select a Cryptocurrency:", font=("Arial", 14)).pack(pady=10)
crypto_combobox = ttk.Combobox(crypto_tab, values=['Bitcoin', 'Ethereum', 'Ripple', 'Litecoin', 'Cardano'])
crypto_combobox.pack(pady=5)
tk.Button(crypto_tab, text="Fetch Crypto", command=display_crypto_data).pack(pady=10)

# Tab 2: Stock Data
stock_tab = ttk.Frame(tab_control)
tab_control.add(stock_tab, text='Stock Data')

tk.Label(stock_tab, text="Select Stock Symbol:", font=("Arial", 14)).pack(pady=10)
stock_combobox = ttk.Combobox(stock_tab, values=['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA'])
stock_combobox.pack(pady=5)
tk.Button(stock_tab, text="Fetch Stock", command=display_stock_data).pack(pady=10)

# Tab 3: Data Analysis
analysis_tab = ttk.Frame(tab_control)
tab_control.add(analysis_tab, text='Data Analysis')

tk.Button(analysis_tab, text="Analyze and Plot Data", command=analyze_and_plot_data).pack(pady=20)


# Result Display Section
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=20)

tab_control.pack(expand=1, fill='both')

root.mainloop()