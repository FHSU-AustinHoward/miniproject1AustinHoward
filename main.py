"""
COMPLETE - (5/5 points) Initial comments with your name, class and project at the top of your .py file.
COMPLETE - (5/5 points) Proper import of packages used.
COMPLETE - (20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your
            favorite stock tickers for the last 10 trading days.
COMPLETE - (10/10 points) Store this information in a list that you will convert to a array in NumPy.
COMPLETE - (10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like
            exploring the documentation for matplotlib. At minimum it just needs to show 10 data points.
COMPLETE - (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your
            project folder, the project should save these when it executes. You may want to add this folder to your
            .gitignore file.
COMPLETE - (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
COMPLETE - (10/10 points) I will be checking out the master branch of your project. Please be sure to include a
            requirements.txt file which contains all the packages that need installed. You can create this
            filled with the output of pip freeze at the terminal prompt.
COMPLETE - (20/20 points) There should be a README.md file in your project that explains what your project is,
            how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of
            Markdown.
"""

# INF601 - Advanced Programming in Python
# Austin Howard
# Mini Project 1

# Imports
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def get_closing(ticker):
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
        stock_closing = np.array(get_closing(stock))
        days = list(range(1, len(stock_closing) + 1))

        plt.plot(days, stock_closing)

        # Get min/max for y axis
        prices = get_closing(stock)
        prices.sort()
        low_price = prices[0]
        high_price = prices[-1]

        plt.title("Closing Price for " + stock)
        plt.xlabel("Days")
        plt.ylabel("Closing Price")
        plt.axis([1, 10, low_price * .99, high_price * 1.01])

        savefile = "charts/" + stock + ".png"
        plt.savefig(savefile)


# Main Function
def main():
    make_dir()
    stocks = set_stocks()
    print_charts(stocks)


# Only run main as stand-alone (not as a module)
if __name__ == "__main__":
    main()