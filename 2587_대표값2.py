import sys

input_num = sys.stdin.readline

list = []
for _ in range(5):
    list.append(int(input_num()))
    
list.sort()
print(int(sum(list)/5))
print(list[2])