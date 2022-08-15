import sys

custum_input = sys.stdin.readline

for _ in range(int(custum_input())):
    A = int(custum_input())
    B = int(custum_input())
    aList = [i for i in range(1, B+1)]
    for i in range(A):
        for j in range(1, B):
            aList[j] += aList[j-1]
    print(aList[B-1])
