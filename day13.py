from numpy.core.numeric import count_nonzero
import pandas as pd
import numpy as np
import re

data = pd.read_csv("data/day13.csv", header = None, dtype=str, delimiter= '\n')[0]
codes = [re.split("\s\S\S\s", word) for word in data.values][1:]

# Challenge 1
word = np.array(data.values)[0]
c_dic = {c[0]:c[1] for c in codes}
c_dic['0'+word[0]] = ''
c_dic[word[-1]+'0'] = ''
word = '0'+word+'0'


steps = 10
dic = {key:0 for key in c_dic}
for i in range(len(word)-1): dic[word[i]+word[i+1]] += 1

for step in range(steps):
    dic2 = {k:val for k, val in dic.items()}
    for key in dic:
        if key[0] != '0' and key[-1] != '0':
            res = c_dic[key]
            dic2[key[0]+res] += dic[key]
            dic2[res+key[1]] += dic[key]
            dic2[key] -= dic[key]
    dic = {k:val for k, val in dic2.items()}

occ = {val:0 for k,val in c_dic.items()}
for char in word: occ[char] = 0

for key in dic:
    occ[key[0]] += dic[key]
    occ[key[1]] += dic[key]
out = np.sort([val for k,val in occ.items()])

print((out[-1]-out[2])//2)


# Challenge 2
word = np.array(data.values)[0]
c_dic = {c[0]:c[1] for c in codes}
c_dic['0'+word[0]] = ''
c_dic[word[-1]+'0'] = ''
word = '0'+word+'0'

steps = 40
dic = {key:0 for key in c_dic}
for i in range(len(word)-1): dic[word[i]+word[i+1]] += 1

for step in range(steps):
    dic2 = {k:val for k, val in dic.items()}
    for key in dic:
        if key[0] != '0' and key[-1] != '0':
            res = c_dic[key]
            dic2[key[0]+res] += dic[key]
            dic2[res+key[1]] += dic[key]
            dic2[key] -= dic[key]
    dic = {k:val for k, val in dic2.items()}

occ = {val:0 for k,val in c_dic.items()}
for char in word: occ[char] = 0

for key in dic:
    occ[key[0]] += dic[key]
    occ[key[1]] += dic[key]
out = np.sort([val for k,val in occ.items()])

print((out[-1]-out[2])//2)