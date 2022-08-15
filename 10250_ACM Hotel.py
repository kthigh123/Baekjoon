import sys

custum_input = sys.stdin.readline
N = int(custum_input())

for _ in range(N):
    A, B, C = map(int, custum_input().split())
    W = (C // A) + 1
    H = C % A
    if C % A == 0:
        W = C//A
        H = A
    print(H*100+W)