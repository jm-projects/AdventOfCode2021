import pandas as pd

data = list(pd.read_csv("data/day1.csv", header = None)[0])

# Challenge 1

total = sum([1 if data[i] < data[i+1] else 0 for i in range(len(data)-1)])
print(total)

# Challenge 2

total2 = sum([1 if data[i] < data[i+3] else 0 for i in range(len(data)-3)])
print(total2)