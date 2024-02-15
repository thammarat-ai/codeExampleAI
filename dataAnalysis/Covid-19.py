# Example 11.15 Covid-19.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns

from matplotlib.ticker import MaxNLocator

# Number of Covid Death
#path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
# Number of Covid Recoveries
#path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
# The latest Covid data
#path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/08-19-2021.csv'

# Number of Confirmed Covid Cases
path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
df = pd.read_csv(path)
df.info()
df.head()

# The country to plot the data for.
country = 'United Kingdom'

# Group by country and sum over the different states/regions of each country.
grouped = df.groupby('Country/Region')
df2 = grouped.sum()
print(df2)

# Start the plot on the day when the number of confirmed cases reaches MIN_CASES.
MIN_CASES = 1

def make_plot(country):
    """Make the bar plot of case numbers and change in numbers line plot."""

    # Extract the Series corresponding to the case numbers for country.
    confirmed = df2.loc[country, df2.columns[3:]]
    print(confirmed)
    # Discard any columns with fewer than MIN_CASES.
    confirmed = confirmed[confirmed >= MIN_CASES].astype(int)
    # Convet index to a proper datetime object
    confirmed.index = pd.to_datetime(confirmed.index)
    n = len(confirmed)
    if n == 0:
        print('Too few data to plot: minimum number of cases is {}'
                .format(MIN_CASES))
        sys.exit(1)

    fig = plt.Figure()

    # Arrange the subplots on a grid
    ax2 = plt.subplot2grid((2,1), (0,0))
    ax1 = plt.subplot2grid((2,1), (1,0))
    ax1.bar(confirmed.index, confirmed.values)
    # Force the x-axis to be in integers (whole number of days) 
    ax1.xaxis.set_major_locator(MaxNLocator(integer=True))

    confirmed_change = confirmed.diff()
    # Running average of daily cases
    sevenday_rolling = confirmed_change.rolling(window=7).mean()
    ax2.plot(confirmed.index, confirmed_change.values, label = 'Daily Cases')
    ax2.plot(confirmed.index, sevenday_rolling.values,'-r', label = '7 Day Average')
    ax2.set_xticks([])
    ax2.legend()

    ax1.set_xlabel('Date ')
    ax1.set_ylabel('Total Confirmed cases, $N$')
    ax2.set_ylabel('Daily Cases $\Delta N$')

    # Add a title reporting the latest number of cases available.
    title = '{}\nTotal {} cases on {}'.format(country, confirmed[-1],
                confirmed.index[-1].strftime('%d %B %Y'))
    plt.suptitle(title)
    

make_plot(country)
plt.show()
print('Today New Cases:', confirmed_change[-1])
print('Today Total Cases:', confirmed[-1])
