import pandas as pd
import numpy as np

data = pd.read_csv("data/day11.csv", header = None, dtype=str)


# Challenge 1

mp = np.array([[int(word[0][i]) for i in range(len(word[0]))] for word in data.values])
mp = np.pad(mp,pad_width=1,mode='constant', constant_values=11)

def spread(m, coord):
    i = coord[0]
    j = coord[1]
    for k in range(-1,2): m[i-k,j+1] += 1 
    for k in range(-1,2): m[i-k,j-1] += 1 
    m[i-1,j] += 1
    m[i+1,j] += 1
    return m
    
    
steps = 100
flashes = 0
for step in range(steps):
    mp += 1
    flashing = True
    c_set = set({})
    while flashing == True:
        flashing = False
        for i in range(1,len(mp)-1):
            for j in range(1, len(mp)-1):
                if mp[i,j] > 9 and (i,j) not in c_set:
                    mp = spread(mp, (i,j))
                    c_set.add((i,j))
                    flashing = True
    
    for i in range(1,len(mp)-1):
        for j in range(1, len(mp)-1):
            if mp[i,j] > 9: 
                mp[i,j] = 0
                flashes += 1

print(flashes)

# Challenge 2

mp = np.array([[int(word[0][i]) for i in range(len(word[0]))] for word in data.values])
mp = np.pad(mp,pad_width=1,mode='constant', constant_values=11)

sync = 1
while sync:
    sync += 1
    flashes = 0
    mp += 1
    flashing = True
    c_set = set({})
    while flashing == True:
        flashing = False
        for i in range(1,len(mp)-1):
            for j in range(1, len(mp)-1):
                if mp[i,j] > 9 and (i,j) not in c_set:
                    mp = spread(mp, (i,j))
                    c_set.add((i,j))
                    flashing = True
    
    for i in range(1,len(mp)-1):
        for j in range(1, len(mp)-1):
            if mp[i,j] > 9: 
                mp[i,j] = 0
                flashes += 1
    if flashes == 100:
        print(sync-1)
        sync = 0