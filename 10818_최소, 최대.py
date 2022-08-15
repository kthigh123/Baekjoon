import sys


input_num = sys.stdin.readline

N = int(input_num())
A = list(map(int, input_num().split))

print(min(A), max(A))