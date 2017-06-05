import urllib.request
import sys
import numpy as np

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
    
# generate summary statistics for col 3
col = 3
coldata = []
for row in xlist:
    coldata.append(float(row[col]))

colarray = np.array(coldata)
colmean = np.mean(colarray)
colstd = np.std(colarray)
print("mean=", colmean, " std=", colstd, "\n")

# calculate quantile boundaries
ntiles = 4
percent_boundary = []

for i in range(ntiles+1):
    percent_boundary.append(np.percentile(colarray, i*(100)/ntiles, interpolation="higher"))

print(percent_boundary)


ntiles = 10
percent_boundary = []

for i in range(ntiles+1):
    percent_boundary.append(np.percentile(colarray, i*(100)/ntiles, interpolation="higher"))

print(percent_boundary)

# the last column contains categorical variables
col = 60
coldata = []
for row in xlist:
    coldata.append(row[col])

unique = set(coldata)
print("unique values = ", unique)

# make unique a list, then give each entry in the list a unique number by using range, then make it a dictionary
catdict = dict(zip(list(unique), range(len(unique))))
catcount = [0] * len(unique)

for elt in coldata:
    catcount[catdict[elt]] += 1
print(list(unique))
print(catcount)


