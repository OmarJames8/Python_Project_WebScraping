# -*- coding: utf-8 -*-
"""Final_Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BLsV7NzKX6HcqL92HRyL3S9M0Bs1BA0C

##Installing  Yfinance libary for Tesla and Gamestop Revenue
"""

# Install yfinance
!pip install yfinance

# Import yfinance
import yfinance as yf

# Create a ticker object for Tesla
tsla = yf.Ticker('TSLA')

# Get historical data for Tesla
tsla_history = tsla.history(period='max')

# Print the first 5 rows of the DataFrame
print(tsla_history.head())

# Reset the index
tsla_history = tsla_history.reset_index()

# Save the dataframe to a CSV file
tsla_history.to_csv('tsla_history.csv', index=False)

# Display the first five rows of the dataframe
print(tsla_history.head())

import pandas as pd
import requests
from bs4 import BeautifulSoup

# define the URL
tesla_url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"

# send a GET request to the URL
tesla_html = requests.get(tesla_url).text

# parse the HTML content using BeautifulSoup
tesla_soup = BeautifulSoup(tesla_html, "html.parser")

tesla_tables = tesla_soup.find_all('table')

for index,table in enumerate(tesla_tables):
    if ("Tesla Quarterly Revenue" in str(table)):
        tesla_table_index = index

tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for row in tesla_tables[tesla_table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col !=[]):
        date = col[0].text
        revenue = col[1].text.replace("$", "").replace(",", "")
        tesla_revenue = tesla_revenue.append({"Date" : date, "Revenue" : revenue}, ignore_index=True)
print(tesla_revenue)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
tesla_revenue

print(tesla_revenue.columns)

import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go

def make_graph(fig, df, x, y, graph_title, x_axis_title, y_axis_title):
    fig.add_trace(go.Scatter(x=df[x], y=df[y], mode='lines', name=graph_title))
    fig.update_layout(title=graph_title, xaxis_title=x_axis_title, yaxis_title=y_axis_title)
    return fig

# define the URL
tesla_url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"

# send a GET request to the URL
tesla_html = requests.get(tesla_url).text

# parse the HTML content using BeautifulSoup
tesla_soup = BeautifulSoup(tesla_html, "html.parser")

tesla_tables = tesla_soup.find_all('table')

for index,table in enumerate(tesla_tables):
    if ("Tesla Quarterly Revenue" in str(table)):
        tesla_table_index = index

tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for row in tesla_tables[tesla_table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col !=[]):
        date = col[0].text
        revenue = col[1].text.replace("$", "").replace(",", "")
        tesla_revenue = tesla_revenue.append({"Date" : date, "Revenue" : revenue}, ignore_index=True)

# convert the 'Revenue' column to numeric values
tesla_revenue['Revenue'] = pd.to_numeric(tesla_revenue['Revenue'])

# use the make_graph function to create a line graph of the revenue data
fig = go.Figure()
fig = make_graph(fig, tesla_revenue, x='Date', y='Revenue', graph_title='Tesla Quarterly Revenue', x_axis_title='Date', y_axis_title='Revenue')
fig.show()

# Display the last five rows of the dataframe
print(tesla_revenue.tail())

# Install yfinance
!pip install yfinance

# Import yfinance
import yfinance as yf

gamestop = yf.Ticker("GME")

gme_data = gamestop.history(period="max")

gme_data.reset_index(inplace=True)
gme_data.head()

gme_url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
gme_html_data = requests.get(gme_url).text

gme_soup = BeautifulSoup(gme_html_data, "html5lib")

gme_tables = gme_soup.find_all('table')

for index,table in enumerate(gme_tables):
    if ("GameStop Quarterly Revenue" in str(table)):
        gme_table_index = index

gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for row in gme_tables[gme_table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col !=[]):
        date = col[0].text
        revenue = col[1].text.replace("$", "").replace(",", "")
        gme_revenue = gme_revenue.append({"Date" : date, "Revenue" : revenue}, ignore_index=True)

gme_revenue.tail()

import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.graph_objs as go

# define the URL
gme_url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"

# send a GET request to the URL
gme_html = requests.get(gme_url).text

# parse the HTML content using BeautifulSoup
gme_soup = BeautifulSoup(gme_html, "html.parser")

# find the table with GameStop revenue data
gme_tables = gme_soup.find_all('table')

for index,table in enumerate(gme_tables):
    if ("GameStop Quarterly Revenue" in str(table)):
        gme_table_index = index

# extract the revenue data from the HTML table and create a pandas DataFrame
gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for row in gme_tables[gme_table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col !=[]):
        date = col[0].text
        revenue = col[1].text.replace("$", "").replace(",", "")
        gme_revenue = gme_revenue.append({"Date" : date, "Revenue" : revenue}, ignore_index=True)

# define the make_graph function
def make_graph(fig, data, x_col, y_col, title, x_title, y_title):
    fig.add_trace(go.Scatter(x=data[x_col], y=data[y_col], name=y_col))
    fig.update_layout(title=title, xaxis_title=x_title, yaxis_title=y_title)
    return fig

# use the make_graph function to create a line graph of the revenue data
fig = go.Figure()
fig = make_graph(fig, gme_revenue, x_col='Date', y_col='Revenue', title='GameStop Quarterly Revenue', x_title='Date', y_title='Revenue')
fig.show()