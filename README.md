# Custom Intelligent Application

This project is a Python-based GUI application that allows users to:

1. Fetch cryptocurrency data from the CoinGecko API.
2. Display stock data for selected stocks.
3. Analyze and visualize stock data with simple plots.

The application is built using the following technologies:
- **Tkinter**: For the graphical user interface (GUI).
- **Requests**: To make HTTP requests to the CoinGecko API.
- **Pandas**: For data manipulation and management.
- **Matplotlib & Seaborn**: For data visualization and analysis.
- **Threading**: To keep the GUI responsive when fetching data from APIs.

## Features

### Cryptocurrency Data
- Users can select a cryptocurrency from a dropdown list (e.g., Bitcoin, Ethereum).
- The app fetches the current price and the 24-hour price change from the CoinGecko API.
- The data is displayed on the screen for the selected cryptocurrency.

### Stock Data
- Users can select a stock symbol (e.g., AAPL, GOOGL, MSFT, AMZN, TSLA).
- Static data for the selected stock, including the closing price and percentage change, is displayed on the screen.

### Data Analysis
- Users can perform basic stock data analysis.
- A bar plot is generated showing stock data for companies like Apple, Google, Microsoft, Amazon, and Tesla.

## Screenshots
### Main Interface
![Cryptocurrency Data](screenshot1.jpg)
### Cryptocurrency Data Fetched
![Cryptocurrency Data Display](screenshot2.jpg)
### Stock Data Fetched
![Stock Data Display](screenshot3.jpg)
### Data Analysis Visualization
![Data Analysis](screenshot4.jpg)

## Setup

### Prerequisites
Make sure you have the following installed:
- **Python 3.x**
- **pip** (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/repository-name.git
   ```

2. Navigate to the project directory:
   ```bash
   cd repository-name
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Required Libraries
You can also install the required packages manually:
```bash
pip install requests pandas matplotlib seaborn
```

### Running the Application

To run the application, execute the following command in the terminal or command prompt:

```bash
python gui_application.py
```

This will launch the GUI, where you can interact with the application to fetch cryptocurrency and stock data or perform data analysis.

## API Information

This application uses the **CoinGecko API** to fetch real-time cryptocurrency data. You do not need an API key to access this data.

- API Documentation: [CoinGecko API](https://www.coingecko.com/en/api)

## Future Enhancements

Some potential improvements that can be added to the application:
- Integration with live stock data API (e.g., Alpha Vantage, Yahoo Finance API).
- More advanced data analysis features, such as historical price charts.
- Add more cryptocurrencies and stock symbols to the dropdown menus.
- Enhance the UI with more customization options.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

