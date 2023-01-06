import sys

input_num = sys.stdin.readline

num = int(input_num())
l = []
for _ in range(num):
    a, b = map(int, input_num().split())
    l.append([a, b])
    
l.sort()

for i in range(len(l)):
    print(f"{l[i][0]} {l[i][1]}")
