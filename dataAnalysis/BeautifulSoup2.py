#Example 11.6 Web scrap Finance with Beautiful Soup
#pip install requests beautifulsoup4 
import pandas as pd
from bs4 import BeautifulSoup
import requests

def get_stock(t):
    url = f'http://finance.yahoo.com/quote/{t}?p={t}'
    res = requests.get(url)
    soup = (BeautifulSoup(res.content, 'lxml'))
    table = soup.find_all('table')[0]
    labels, data = pd.read_html(str(table))[0].values.T
    return pd.Series(data, labels, name = t)

stock_name = ["AAPL","AMZN","GOOG","TSLA"]
df = pd.concat(map(get_stock, stock_name), axis=1)
print(df.T)
