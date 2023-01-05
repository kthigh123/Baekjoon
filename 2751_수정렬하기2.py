import sys

input_num = sys.stdin.readline

num = int(input_num())
a = []

for i in range(num):
    a.append(int(input_num()));
a.sort()
for i in a:
    print(i)