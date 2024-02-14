import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

df = pd.read_csv('data.csv')
print(df)
x = df['x']
y = df['y']

slope, intercept, r, p, std_err = stats.linregress(x, y)
print("slope: ", slope)
print("intercept: ", intercept)
print("std_err: ", std_err)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y, label='Data')
plt.plot(x, mymodel, "r", label='Regression Line')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.show()