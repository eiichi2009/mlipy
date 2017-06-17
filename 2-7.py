#!/usr/bin/env python

__author__ = "eii"
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt


target_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"

d = pd.read_csv(target_url, header=None, prefix="V")

# calculate correlation between two real valued attributes
attr1 = d.iloc[0,0:60]
attr30 = d.iloc[29,0:60]

plt.scatter(attr1, attr30)
plt.xlabel("attribute 1")
plt.ylabel("attribute 29")
plt.show()
