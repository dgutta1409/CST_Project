import tkinter as tk  # Import the tkinter library for GUI
from tkinter import ttk, messagebox  # Import specific modules from tkinter
import requests  # For making API requests to fetch data
import pandas as pd  # For working with data in DataFrames
import matplotlib.pyplot as plt  # For plotting graphs
import seaborn as sns  # For advanced plotting
from threading import Thread  # To run processes in parallel (threads)

# Function to fetch cryptocurrency data from the CoinGecko API
def fetch_crypto_data(coin):
    url = f"https://api.coingecko.com/api/v3/coins/{coin}"  # API URL
    try:
        response = requests.get(url)  # Request data from the API
        response.raise_for_status()  # Raise an exception if the request fails
        return response.json()  # Return the API response as JSON
    except requests.exceptions.RequestException as e:  # Handle errors
        messagebox.showerror("Error", f"Unable to fetch cryptocurrency data: {e}")
        return None

# Function to display cryptocurrency data in the GUI
def display_crypto_data():
    coin = crypto_combobox.get().lower().replace(" ", "-")  # Get the selected cryptocurrency
    if not coin:  # Check if the user selected a valid cryptocurrency
        messagebox.showwarning("Input Error", "Please select a cryptocurrency.")
        return
    result_label.config(text="Fetching crypto data...")  # Show a loading message
    # Run the update_crypto_data function in a separate thread to avoid freezing the GUI
    Thread(target=lambda: update_crypto_data(fetch_crypto_data(coin))).start()

# Function to analyze and plot data
def analyze_and_plot_data():
    data = {
        'Parameter': ['Apple', 'Google', 'Microsoft', 'Amazon', 'Tesla'],
        'Value': [150, 2800, 300, 3400, 700]
    }
    df = pd.DataFrame(data)  # Create a DataFrame for the analysis

    plt.figure(figsize=(6, 4))  # Set the figure size for the plot
    sns.barplot(x='Parameter', y='Value', data=df)  # Create a bar plot
    plt.title('Stock Data Analysis') 
# Function to update the GUI with cryptocurrency data
def update_crypto_data(data):
    if data:
        price = data['market_data']['current_price']['usd']  # Get the price
        change = data['market_data']['price_change_percentage_24h']  # Get the 24h change
        crypto_info = f"{data['name']}:\nPrice: ${price:.2f}\n24h Change: {change:.2f}%"  # Display the data
        result_label.config(text=crypto_info)  # Update the result label with the info

# Static stock data for demonstration purposes
stock_data = {
    'stock_symbol': ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA'],
    'closing_price': [150, 2800, 300, 3400, 700],
    'change_percentage': [1.5, 0.5, 2.0, -0.5, 3.2]
}
df_stock = pd.DataFrame(stock_data)  # Create a DataFrame for stock data

# Function to analyze and plot data
def analyze_and_plot_data():
    data = {
        'Parameter': ['Apple', 'Google', 'Microsoft', 'Amazon', 'Tesla'],
        'Value': [150, 2800, 300, 3400, 700]
    }
    df = pd.DataFrame(data)  # Create a DataFrame for the analysis

    plt.figure(figsize=(6, 4))  # Set the figure size for the plot
    sns.barplot(x='Parameter', y='Value', data=df)  # Create a bar plot
    plt.title('Stock Data Analysis')  # Set the plot title
    plt.show()  # Show the plot

# GUI Setup
root = tk.Tk()  # Create the main window
root.title("Custom Intelligent Application")  # Set the window title
root.geometry("600x400")  # Set the window size

tab_control = ttk.Notebook(root)  # Create tab control

# Tab 1: Cryptocurrency Data
crypto_tab = ttk.Frame(tab_control)
tab_control.add(crypto_tab, text='Cryptocurrency Data')  # Add tab for cryptocurrency

# Tab 2: Stock Data
stock_tab = ttk.Frame(tab_control)
tab_control.add(stock_tab, text='Stock Data')  # Add tab for stock data

tk.Label(stock_tab, text="Select Stock Symbol:", font=("Arial", 14)).pack(pady=10)
stock_combobox = ttk.Combobox(stock_tab, values=['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA'])
stock_combobox.pack(pady=5)
tk.Button(stock_tab, text="Fetch Stock", command=display_stock_data).pack(pady=10)
tk.Label(crypto_tab, text="Select a Cryptocurrency:", font=("Arial", 14)).pack(pady=10)
crypto_combobox = ttk.Combobox(crypto_tab, values=['Bitcoin', 'Ethereum', 'Ripple', 'Litecoin', 'Cardano'])
crypto_combobox.pack(pady=5)
tk.Button(crypto_tab, text="Fetch Crypto", command=display_crypto_data).pack(pady=10)

# Tab 3: Data Analysis
analysis_tab = ttk.Frame(tab_control)
tab_control.add(analysis_tab, text='Data Analysis')  # Add tab for data analysis

tk.Button(analysis_tab, text="Analyze and Plot Data", command=analyze_and_plot_data).pack(pady=20)

# Result Display Section
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=20)

tab_control.pack(expand=1, fill='both')  # Pack the tab control to fill the window

root.mainloop()  # Run the main event loop
