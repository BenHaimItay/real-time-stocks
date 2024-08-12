# Real-Time Stocks

Real-Time Stocks is a Python application that fetches and displays real-time stock data using the Interactive Brokers API and visualizes it using lightweight charts.

## Features

- Fetch real-time stock data from Interactive Brokers.
- Visualize stock data with interactive charts.
- Command-line interface for easy interaction.

## Requirements

- Python > 3.10
- Poetry for dependency management

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/real-time-stocks.git
    cd real-time-stocks
    ```

2. Install dependencies using Poetry:

    ```sh
    poetry install
    ```

3. Assure IBKR account and Trader Workstation running in background

## Usage

To run the application, use the following command:

```sh
poetry run main.py <STOCK_SYMBOL>
```
