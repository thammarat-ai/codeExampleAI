#Example 11.2 SVR Regression
import matplotlib.pyplot as plt
from scipy import stats
import pandas 

df = pandas.read_csv('data.csv')
print(df)
x1 = df['Time'].values.reshape(-1,1)
y1 = df['Voltage'].values.reshape(-1,1)
print(x1)
print(y1)


from sklearn.svm import SVR
lr = SVR(kernel = 'linear', C =1000.0)
pr = SVR(kernel = 'poly', C =1000.0, degree = 2)
rr = SVR(kernel = 'rbf', C =1000.0, gamma = 0.85)
lr.fit(x1,y1)
pr.fit(x1,y1)
rr.fit(x1,y1)

plt.figure()
plt.scatter(x1, y1, color='r', label='Data')
plt.plot(x1, lr.predict(x1),label='linear SVR')
plt.plot(x1, pr.predict(x1),label='poly SVR')
plt.plot(x1, rr.predict(x1),label='rbf SVR')
plt.legend()
plt.show()
