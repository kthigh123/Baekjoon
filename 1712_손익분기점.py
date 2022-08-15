import sys

custum_input = sys.stdin.readline

def math(A, B, C):
    n = 1
    if C > B:
        while A+B*n >= C*n:
            n += 1
    else:
        n = -1
    return n

A, B, C = map(int, custum_input().split())

print(math(A, B, C))
