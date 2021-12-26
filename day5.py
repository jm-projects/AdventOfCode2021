import pandas as pd
import re
import numpy as np

data = pd.read_csv("data/day5.csv", header = None, sep='\n', engine='python')[0]

class Line():
    def __init__(self, start_coords, end_coords):
        self.start = start_coords
        self.end = end_coords
        if self.start[0] == self.end[0]:
            self.straight = True
            self.orientation = 'vert'
        elif self.start[1] == self.end[1]:
            self.straight = True
            self.orientation = 'hori'
        elif self.start[1] - self.end[1] == self.start[0] - self.end[0]:
            self.orientation = 'd_up'
        else:
            self.orientation = 'd_down'
            
def return_points(l:Line, hmap):
    if l.orientation == 'hori':
        m = np.sort([l.start[0], l.end[0]])
        for coord in [[i,l.start[1]] for i in range(m[0], m[1]+1)]:
            hmap[coord[0], coord[1]] += 1
    elif l.orientation =='vert':
        m = np.sort([l.start[1], l.end[1]])
        for coord in [[l.start[0], i] for i in range(m[0], m[1]+1)]:
            hmap[coord[0], coord[1]] += 1
    elif l.orientation == 'd_up':
        m = np.sort([l.start[0], l.end[0]])
        n = np.sort([l.start[1], l.end[1]])
        for coord in [[m[0]+i,n[0]+i] for i in range(0, n[1]-n[0]+1)]:
            hmap[coord[0], coord[1]] += 1
    else:
        m = np.sort([l.start[0], l.end[0]])
        n = np.sort([l.start[1], l.end[1]])
        for coord in [[m[0]+i,n[1]-i] for i in range(0, n[1]-n[0]+1)]:
            hmap[coord[0], coord[1]] += 1
    return hmap
            
inst = [re.split("\s\S\S\s", word) for word in data]
inst = [[re.split(",", word[0]), re.split(",", word[1])] for word in inst]
inst = [[[int(word[0][0]), int(word[0][1])], [int(word[1][0]), int(word[1][1])]] for word in inst]

lines = [Line(l[0], l[1]) for l in inst]

# Challenge 1
        
s_lines = [l for l in lines if (l.orientation == 'hori' or l.orientation == 'vert')]
hashmap = np.tile(0, (1000,1000))
for l in s_lines:
    hashmap = return_points(l, hashmap)
print(np.sum(hashmap > 1))

# Challenge 2

hashmap = np.tile(0, (1000,1000))
for l in lines:
    hashmap = return_points(l, hashmap)
print(np.sum(hashmap > 1))