from typing import List
import pandas as pd
import numpy as np

data = pd.read_csv("data/day10.csv", header = None, dtype=str)[0]
brack_list = np.array(data)

# Challenge 1

def bracket_finder(word):
    stack = []
    dic = {')':'(',']':'[','}':'{','>':'<'}
    for bracket in word:
        if bracket in dic.values():
            stack.append(bracket)
        elif dic[bracket] == stack[-1]:
            stack = stack[:-1]
        else:
            return bracket
    return None

score_map = {')':3,']':57,'}':1197,'>':25137}
score = sum([score_map[bracket_finder(word)] for word in brack_list if bracket_finder(word) != None ])
print(score)

# Challenge 2

def bracket_fixer(word):
    stack = []
    dic = {')':'(',']':'[','}':'{','>':'<'}
    for bracket in word:
        if bracket in dic.values():
            stack.append(bracket)
        elif dic[bracket] == stack[-1]:
            stack = stack[:-1]
    return [{v:k for k,v in dic.items()}[br] for br in stack[::-1]]

score_map = {')':1,']':2,'}':3,'>':4}
scores = []
for word in brack_list:
    score = 0
    if bracket_finder(word) == None:
        for br in bracket_fixer(word):
            score *= 5
            score += score_map[br]
        scores.append(score)
print(np.sort(scores)[len(scores)//2])