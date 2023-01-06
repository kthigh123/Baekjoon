import sys

input_num = sys.stdin.readline

a = input_num().strip()
b = []
for i in a:
    b.append(int(i))
    
b.sort(reverse=True)
for i in b:
    print(i, end='')
