#!/usr/bin/env python

__author__ = "eii"
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt


target_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"

d = pd.read_csv(target_url, header=None, prefix="V")
for i in range(len(d)):
    if d.iat[i,60] == "M":
        col = "red"
    else:
        col = "blue"
    d_row = d.iloc[i,0:60]
    d_row.plot(color=col)

plt.xlabel("index")
plt.ylabel("value")
plt.show()
    
