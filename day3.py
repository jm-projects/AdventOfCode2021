from typing import List
import pandas as pd

data = list(pd.read_csv("data/day3.csv", header=None, dtype=str)[0])

# Challenge 1

cols = [[int(num[i]) for num in data] for i in range(len(data[0]))]
g_str = [1 if sum(col)/len(col) > 0.5 else 0 for col in cols]
g = sum([g_str[i]*2**(len(g_str)-i-1) for i in range(len(g_str))])
print((2**len(data[0])-1-g)*g)

# Challenge 2


def solver(d: List[str], sign: int, rec: int = 0) -> int:
    """Calculates the CO2 or Oxygen scrubber rating as specified
    in the advent puzzle.
    :param d: diagnostic binary data
    :param sign: 1 if calculating Oxy Oxygen, 0 for CO2
    :param rec: recursion parameter"""

    if len(d) == 1:
        return sum([int(d[0][i])*2**(len(d[0])-i-1) for i in range(len(d[0]))])
    else:
        c = [int(num[rec]) for num in d]
        if sign and sum(c)/len(c) >= 0.5:
            key = 0
        elif not sign and sum(c)/len(c) < 0.5:
            key = 0
        else:
            key = 1
        d2 = [num for num in d if num[rec] == str(key)]
        rec += 1
        return solver(d2, sign, rec)


print(solver(data, 1)*solver(data, 0))
