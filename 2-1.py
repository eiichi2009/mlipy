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

print("Number of rows of data = ", len(xlist), "\n")
print("Number of rows of data = ", len(xlist[1]), "\n")
