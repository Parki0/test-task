import sys
path = sys.argv[1:][0]
# A:\common textbook 2\code\job testing\nums.txt
with open(path) as f:
    lines = f.readlines()
lines = list(map(lambda x: int(x), lines))

inp = lines

from math import ceil
mid = ceil((max(inp)-min(inp))/2) + min(inp)

result = list(map(lambda x: max(x, mid) - min(x, mid), inp))

print(sum(result)) 