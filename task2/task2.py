def relation_from_zero(x,y,r):
    if (x*x) + (y*y) == r*r:
        return 0
    elif (x*x) + (y*y) < r*r:
        return 1
    else:
        return 2

import sys
paths = sys.argv[1:]


with open(paths[0]) as f:
    lines = f.readlines()

circle_coors = lines[0].split(' ')

circle_x = int(circle_coors[0])
circle_y = int(circle_coors[1])
circle_r = int(lines[1])

with open(paths[1]) as f:
    coors_raw = f.readlines()

coors_raw2 = list(map(lambda n: n.split(' '),coors_raw))

coors = list(map(lambda n: list(map(lambda n2: int(n2),n)),coors_raw2))

for c in coors:
    print(relation_from_zero(c[0]-circle_x,c[1]-circle_y,circle_r))