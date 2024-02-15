import pandas as pd
#Global CO2 data
df = pd.read_csv('https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2/co2_mm_gl.csv', comment='#')

print(df.head())
dl = df['average'].values.tolist()
df = pd.Series(dl, index=pd.date_range('1-1-1980', periods=len(df), freq='M'), name = 'CO2')
print(df.head())
df.describe()


from statsmodels.tsa.seasonal import STL
stl = STL(df)
res = stl.fit()
fig = res.plot()
fig.show()

#Predition =====================================================================
from statsmodels.tsa.forecasting.stl import STLForecast
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

data = df
stlf = STLForecast(data , ARIMA, model_kwargs={"order": (2, 1, 0)})
res = stlf.fit()

forecast = res.forecast(24)
plt.figure()
plt.plot(data)
plt.plot(forecast)
plt.show()
