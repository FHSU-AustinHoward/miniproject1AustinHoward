# Please submit a link to your GitHub project. Do not submit your project files here.
# This project will be using the packages NumPy and Matplotlib in order to create 5 graphs that output as PNG files.

# COMPLETE - (5/5 points) Initial comments with your name, class and project at the top of your .py file.
# COMPLETE - (5/5 points) Proper import of packages used.
# INCOMPLETE - (20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your
# favorite stock tickers for the last 10 trading days.
# INCOMPLETE - (10/10 points) Store this information in a list that you will convert to a array in NumPy.
# INCOMPLETE - (10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like
# exploring the documentation for matplotlib. At minimum it just needs to show 10 data points.
# INCOMPLETE - (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your
# project folder, the project should save these when it executes. You may want to add this folder to your .gitignore
# file.
# INCOMPLETE - (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# INCOMPLETE - (10/10 points) I will be checking out the master branch of your project. Please be sure to include
# a requirements.txt file which contains all the packages that need installed. You can create this filled with the
# output of pip freeze at the terminal prompt.
# INCOMPLETE - (20/20 points) There should be a README.md file in your project that explains what your project is,
# how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.

# INF601 - Advanced Programming in Python
# Austin Howard
# Mini Project 1

# Imports
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# Function to gather stock information
def getClosing(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period='10d')

    closing_list = []

    for price in hist['Close']:
        closing_list.append(price)

    print(closing_list)
    return closing_list

stocks = ["TM", "HMC", "F", "GM", "TSLA"]
stocks = np.array(stocks)

plt.plot(stocks)
plt.show()