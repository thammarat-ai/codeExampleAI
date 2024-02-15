#Example 11.4 - html5lib library
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import numpy as np

#pip install html5lib
df = pd.read_html('https://en.wikipedia.org/wiki/World_population')
print(f'Total tables: {len(df)}')
df = pd.read_html('https://en.wikipedia.org/wiki/World_population', match='Global annual population growth')
df =df[0]

x = df['Year'].astype('float')
y = df['Population'].astype('float')

plt.scatter(x, y)
plt.show()  
