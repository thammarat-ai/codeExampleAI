#Example 11.1 Linear Regression
import matplotlib.pyplot as plt
from scipy import stats
import pandas 

df = pandas.read_csv('data.csv')
print(df)
x = df['Time']
y = df['Voltage']


slope, intercept, r, p, std_err = stats.linregress(x, y)
print("slope: ", slope)
print("intercept: ", intercept)
print("std_err: ", std_err)
def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y,label="data")
plt.plot(x, mymodel, "r",label="fitted line")
plt.xlabel("Time")
plt.ylabel("Voltage")
plt.legend()
plt.show()

