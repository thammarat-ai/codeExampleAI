# Example 11.7 Linear Regression from a folder
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

from os import listdir
from os.path import isfile, join

def myFit(file):
    df = pd.read_csv(file)
    #print(df.columns)
    x = df[df.columns[0]]
    y = df[df.columns[1]]

    slope, intercept, r, p, std_err = stats.linregress(x, y)
    print(file)
    print("slope: ", slope)
    print("intercept: ", intercept)
    print("std_err: ", std_err)
    
    def myfunc(x):
        return slope * x + intercept
    mymodel = list(map(myfunc, x))
    plt.figure()
    plt.scatter(x, y, label='original data')
    plt.plot(x, mymodel, "r", label='fitted line')
    plt.title(file)
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])
    plt.legend()

mypath = "./datasets"
files = [join(mypath, f) for f in listdir(mypath) if f.split(".")[-1] =="csv"]
#print(files)
   
for file in files:
    myFit(file)
plt.show()
