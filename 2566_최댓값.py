#0인경우를 생각해야 하는 문제

import sys

input_num = sys.stdin.readline

a = []
b = [0, 1, 1]

for i in range(9):
    a = (list(map(int, input_num().strip().split())))
    if (max(a) > b[0]):
        b[0] = max(a)
        b[1] = i + 1
        b[2] = a.index(max(a)) + 1
    
print(b[0])
print(f"{b[1]} {b[2]}")
