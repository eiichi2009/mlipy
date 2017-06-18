#!/usr/bin/env python3.6

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from math import exp

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"

abalone = pd.read_csv(url, header=None, prefix="V")
abalone.columns = ["Sex", "Lenght", "Diameter", "Height", "Whole Wt", "Shucked Wt", "Viscera Wt", "Shell Wt", "Ringe"]

summary = abalone.describe()
print(summary)

nrows = len(abalone.index)
print(abalone.index)
minrings = summary.iloc[3,7]
maxrings = summary.iloc[7,7]

for i in range(1000):
    datarow = abalone.iloc[i,1:8]
    labelcolor = (abalone.iloc[i,8] - minrings) / (maxrings - minrings)
    datarow.plot(color=plt.cm.RdYlBu(labelcolor), alpha=0.5)

plt.xlabel("index")
plt.ylabel("value")
plt.show()    
