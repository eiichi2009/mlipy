#!/usr/bin/env python3.6

import pandas as pd
from pandas import *
from pylab import *
import matplotlib.pyplot as plt

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
wine = pd.read_csv(url, header=0, sep=";")
print(wine.head())

summary = wine.describe()
print(summary)

wine_normalized = wine

ncols = len(wine.columns)
for i in range(ncols):
    col_len = len(wine.iloc[:,i])
    col_mean = wine.iloc[:,i].mean()
    col_std = wine.iloc[:,i].std()
    for j in range(col_len):
        wine_normalized.iloc[j,i] = (wine.iloc[j,i] - col_mean) / col_std

arr = wine_normalized.values
boxplot(arr)
show()
