import csv
import numpy as np

# Training data
o2 = [
    ["<=30", "<=30", "31...40", ">40", ">40", ">40", "31...40",
        "<=30", "<=30", ">40", "<=30", "31...40", "31...40", ">40"],
    ["high", "high", "high", "medium", "low", "low", "low", "medium",
     "low", "medium", "medium", "medium", "high", "medium"],
    [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    ["fair", "excellent", "fair", "fair", "fair", "excellent",
     "excellent", "fair", "fair", "fair", "excellent", "excellent", "fair", "excellent"],
    [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0]
]

# What we know
r = ["<=30", "medium", 1, "fair"]

# a = []
# with open('train_data1.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         a.append(row[0].split(","))

# o = np.array(a).T.tolist()

# print(o)
# print(o2)

import pandas as pd 

file_handler = open("train_data1.csv", "r") 
data = pd.read_csv(file_handler, sep = ",") 
file_handler.close() 
  
print(data)