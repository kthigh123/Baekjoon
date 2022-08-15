import sys


input_num = sys.stdin.readline
N, X = map(int, input_num().split())
A = list(map(int, input_num().split()))

for i in A:
    if i<X:
        print(i, end=" ")