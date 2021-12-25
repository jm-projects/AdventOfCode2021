import pandas as pd
import re

data = list(pd.read_csv("data/day2.csv", header = None)[0])

# Challenge 1

f = sum([int(re.split("\s", inst)[1]) if re.split("\s", inst)[0][0]=='f' else 0 for inst in data])
rem_f = [inst for inst in data if re.split("\s", inst, 1)[0][0] != 'f']
d = sum([-int(re.split("\s", inst)[1]) if re.split("\s", inst, 1)[0]=='up' else int(re.split("\s", inst)[1]) for inst in rem_f])
print(d*f)

# Challenge 2

aim, f, d = 0, 0, 0
for word in data:
    inst = re.split("\s", word)[0]
    mag = int(re.split("\s", word)[1])
    if inst[0]=='f':
        f += mag
        d += aim*mag
    elif inst[0]=='u':
        aim -= mag
    else:
        aim += mag
print(d*f)