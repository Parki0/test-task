def round(length):

    def calc_round(num):
        return (num-1) % length + 1

    return calc_round
###################

import sys
sys_args = sys.argv[1:]

length        = int(sys_args[0])
original_path = int(sys_args[1])

calc_round = round(length)

path = original_path - 1
out = [1]

while not (len(out) > 1 and out[-1] == 1):
    out.append( calc_round(out[-1] + path) )

out.pop()

print("".join([str(x) for x in out]))