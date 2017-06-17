#!/usr/bin/env python

__author__ = "eii"
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"
d = pd.read_csv(url, header=None, prefix="V")
cormat = DataFrame(d.corr())

plt.pcolor(cormat)
plt.show()
