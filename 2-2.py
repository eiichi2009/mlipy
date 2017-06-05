import urllib.request
import sys

# read data from url
target_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"

data = urllib.request.urlopen(target_url).read().decode("utf-8")
xlist = []
labels = []
for line in data.splitlines():
    row = line.strip().split(",")
    xlist.append(row)

nrow = len(xlist)
ncol = len(xlist[0])
    
type = [0] * 3
colCounts = []

for col in range(ncol):
    for row in xlist:
        try:
            a = float(row[col])
            if isinstance(a, float):
                type[0] += 1
        except ValueError:
            if len(row[col]) > 0:
                type[1] += 1
            else:
                type[2] += 1
    colCounts.append(type)
    type = [0] * 3

print("col#:", "\t", "Number", "\t\t", "strings", "\t\t", "Other")
icol = 0
for types in colCounts:
    print(icol, "\t\t", types[0], "\t\t", types[1], "\t\t", types[2])
    icol += 1
