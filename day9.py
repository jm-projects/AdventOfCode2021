import pandas as pd
import numpy as np

data = pd.read_csv("data/day9.csv", header = None, dtype=str)

mp = np.array([[int(word[0][i]) for i in range(len(word[0]))] for word in data.values])

# Challenge 1

mp = np.pad(mp,pad_width=1,mode='maximum')
l = []
for i in range(1,len(mp)-1):
    for j in range(1,len(mp[0])-1):
        if mp[i,j] < min([mp[i+1,j], mp[i-1,j], mp[i,j+1], mp[i,j-1]]):
            l.append(mp[i,j]+1)
print(sum(l))

# Challenge 2

def spreader(m) -> int:
    c=1
    spreading = 1
    while spreading == True:
        spreading = 0
        for i in range(1,len(m)-1):
            for j in range(1,len(m[0])-1):
                if m[i,j] == -1:
                    m[i,j] = -2
                    a = {(i+1,j):m[i+1,j], (i-1,j):m[i-1,j], (i,j+1):m[i,j+1], (i,j-1):m[i,j-1]}
                    infected = [key for key, ele in a.items() if (ele < 9 and ele > -1)]
                    c += len(infected)
                    spreading = 1
                    for key in infected:
                        m[key[0], key[1]] = -1
    return (m,c)
                        
pits = []
for i in range(1,len(mp)-1):
    for j in range(1,len(mp)-1):
        if mp[i,j] < 9 and mp[i,j] > -1:
            mp[i,j] = -1
            mp, size = spreader(mp)
            pits.append(size)

print(np.sort(pits)[-1]*np.sort(pits)[-2]*np.sort(pits)[-3])