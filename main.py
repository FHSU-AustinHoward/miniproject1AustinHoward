# INF601 - Advanced Programming in Python
# Austin Howard
# Mini Project 1

# Imports
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import warnings

from pathlib import Path


def get_closing(ticker):
    # Ignore the pesky pandas FutureWarning
    warnings.simplefilter(action="ignore", category=FutureWarning)

    # Get the closing price for the last 10 trading days
    stock = yf.Ticker(ticker)
    hist = stock.history(period='10d')

    # Create a list for the closing price, append closing prices
    closing_list = []
    for price in hist['Close']:
        closing_list.append(price)

    return closing_list


def make_dir():
    # Attempt to make a directory for the charts...
    try:
        Path('charts').mkdir()
    # ...unless it already exists
    except FileExistsError:
        pass


def set_stocks():
    stocks = ["TM", "HMC", "F", "GM", "TSLA"]
    return stocks


def print_charts(stocks):
    for stock in stocks:
        # Get the day and closing price for each stock
        stock_closing = np.array(get_closing(stock))
        days = list(range(1, len(stock_closing) + 1))

        # Create the graph
        plt.plot(days, stock_closing)

        # Format the graph, visually
        plt.title(f"Closing Price for {stock}")
        plt.xlabel("Days")
        plt.ylabel("Closing Price")
        plt.xticks(np.arange(1, len(stock_closing) + 1, step=1))

        # Save the graph to the charts folder and then clear it
        savefile = "charts/" + stock + ".png"
        plt.savefig(savefile)
        plt.clf()


# Main Function
def main():
    make_dir()
    stocks = set_stocks()
    print_charts(stocks)


# Only run main as stand-alone (not as a module)
if __name__ == "__main__":
    main()