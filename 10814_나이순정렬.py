import sys

input_num = sys.stdin.readline

list = []
for i in range(int(input_num())):
    x, y = map(str, input_num().split())
    list.append([int(x), i, y])
    
list.sort()
for i in list:
    print(f"{i[0]} {i[2]}")