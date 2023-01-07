import sys

input_num = sys.stdin.readline

a = []
for _ in range(int(input_num())):
    x, y = map(int, input_num().split())
    a.append([y, x])
    
a.sort()
for i in a:
    print(f"{i[1]} {i[0]}")