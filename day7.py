import numpy as np
import pandas as pd

data = pd.read_csv("data/day7.csv", header = None)
crabs = np.array(data.values)[0]

# Challenge 1

print(min([np.sum(np.abs(crabs-i)) for i in range(min(crabs), max(crabs))]))

# Challenge 2

print(min([np.sum(np.abs(crabs-i)*(np.abs(crabs-i)+1)//2) for i in range(min(crabs), max(crabs))]))
