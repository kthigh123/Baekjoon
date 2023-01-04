import sys

input_num = sys.stdin.readline

n = [int(input_num()) for _ in range(9)] #list comprehension
print(f"{max(n)}\n{n.index(max(n))+1}")
