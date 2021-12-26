import numpy as np
import numpy as np
import pandas as pd
import time
data = pd.read_csv("data/day6.csv", header = None)

# Challenge 1

total_t = 80
fish = np.array(data.values)[0]
for day in range(total_t):
    new = len(fish)- np.count_nonzero(fish)
    fish = fish + (fish == 0)*7 - 1
    fish = np.append(fish, new*[8])
print(len(fish))

# Challenge 2

total_t = 256
fish = np.array(data.values)[0]
fishmap = {i:np.count_nonzero(fish==i) for i in range(0,9)}
for day in range(total_t):
    new = fishmap[0]
    fishmap = {i:fishmap[i+1] for i in range(0,8)}
    fishmap[8] = new
    fishmap[6] += new
print(sum([fishmap[i] for i in range(0,9)]))