#!/usr/bin/env python

__author__ = "eii"
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import math
import sys
import random

def corr(x,y):
    if len(x) != len(y):
        print("data number does not match")
        return -100
    
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)
    x_delta = []
    y_delta = []
    for i in range(len(x)):
        x_delta.append(x[i] - x_mean)
        y_delta.append(y[i] - y_mean)
    x_delta_2 = 0.0
    y_delta_2 = 0.0
    xy_2 = 0.0
    for i in range(len(x)):
        x_delta_2 += x_delta[i] ** 2
        y_delta_2 += y_delta[i] ** 2
        xy_2 += x_delta[i]*y_delta[i]
    return xy_2 / math.sqrt(x_delta_2 * y_delta_2)


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"
d = pd.read_csv(url, header=None, prefix="V")

# calculate correlations between two rows
row2 = list(d.iloc[1,0:60])     # row1, col0-59
row3 = list(d.iloc[2,0:60])     # row6, col0-59
row21 = list(d.iloc[20,0:60])

print("row2 and row3 correlation = ", corr(row2,row3), "\n")
print("row2 and row21 correlation = ", corr(row2,row21), "\n")

x = []
y = []
for i in range(1000):
    p = random.randint(1,100)
    x.append(p)
    if p % 2 == 0:
        y.append(0)
    else:
        y.append(1)

print("x and y = ", corr(x,y))    
