__author__ = "eii"

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

target_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"

data = pd.read_csv(target_url, header=None, prefix="V")
print(data.head())
print(data.tail())

summary = data.describe()
print(summary)

