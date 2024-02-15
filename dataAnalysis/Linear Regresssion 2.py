#Example 11.3 Linear Regression
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

#df = pd.read_csv('data.csv')
#wine_names = ['Class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315', 'Proline']
#df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', names = wine_names)

#df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data')
#df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data', header=None)
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/00291/airfoil_self_noise.dat', sep="\t", names = ['Frequency','Angle of attack','Chord length','Free-stream velocity','Suction/side','Scaled/sound']) 

print(df)
#print(df.head())
#print(df.describe())


x = df['Frequency']
y = df['Scaled/sound']


slope, intercept, r, p, std_err = stats.linregress(x, y)
print("slope: ", slope)
print("intercept: ", intercept)
print("std_err: ", std_err)
def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y, label='original data')
plt.plot(x, mymodel, "r", label='fitted line')
plt.xlabel("Time")
plt.ylabel("Voltage")
plt.legend()
plt.show()
