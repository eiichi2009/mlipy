#!/usr/bin/env python

__author__ = "eii"
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt


target_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"

d = pd.read_csv(target_url, header=None, prefix="V")
length = len(d)

target = []
for i in range(length):
    if d.iat[i,60] == "M":
        target.append(1.0)
    else:
        target.append(0.0)

# plot 35th attribute
attr35 = d.iloc[0:length, 34]
plt.scatter(attr35, target)
plt.show()
