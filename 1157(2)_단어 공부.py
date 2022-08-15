#두 번째 Solution(더 효율적)

import sys
num_input = sys.stdin.readline

N = list(map(str, num_input().strip().upper()))
total = {}

for i in N:
    if i in total:
        total[i] += 1
    else:
        total[i] = 1

temp = [key for key, value in total.items() if max(total.values()) == value]

if len(temp) == 1:
    print(temp[0])
else:
    print("?")



