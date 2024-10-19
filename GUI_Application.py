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
