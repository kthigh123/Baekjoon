import sys

num_input = sys.stdin.readline

A, B = map(int, num_input().split())

A = A//100+A%100//10*10+A%10*100 #Change right and left numbers
B = B//100+B%100//10*10+B%10*100 

if A>B:
    print(A)
else:
    print(B)