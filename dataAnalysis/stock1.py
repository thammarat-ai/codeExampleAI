#Example 11.9 Get Stock Data from Yahoo
from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd


symbol = 'MSFT'           #'AMZN','AAPL', 'GOOGL'
data_source='yahoo'       #'google'
start_date = '2016-01-01'
end_date = '2021-01-01'

df = data.DataReader(symbol, data_source, start_date, end_date)
#print(df)
close = df['Close']
#print(close)
#print(close.head(10))
#print(close.describe())

# Calculate the 20 and 100 days moving averages
short_rolling = close.rolling(window=20).mean()
long_rolling = close.rolling(window=100).mean()

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Calculate the 'buy' and 'sell' signals and positions
df['Signal'] = 0.0
df['Signal'] = np.where(short_rolling > long_rolling, 1.0, 0.0)
df['Position'] = df['Signal'].diff()

# Plot the data
fig, ax = plt.subplots(figsize=(16,9))
ax.plot(close.index, close, label=symbol)
ax.plot(short_rolling.index,  short_rolling, label='20 days rolling')
ax.plot(long_rolling.index, long_rolling, label='100 days rolling')

# plot 'buy' signals
plt.plot(df[df['Position'] == 1].index,
         short_rolling[df['Position'] == 1],
         '^', markersize = 15, color = 'g', label = 'buy')

# plot 'sell' signals
plt.plot(df[df['Position'] == -1].index, 
         short_rolling[df['Position'] == -1],
         'v', markersize = 15, color = 'r', label = 'sell')
ax.set_xlabel('Date')
ax.set_ylabel('Closing price ($)')
ax.legend()
plt.show()
