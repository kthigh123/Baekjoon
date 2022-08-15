import sys

custum_input = sys.stdin.readline

for _ in range(int(custum_input())):
    A = int(custum_input())
    B = int(custum_input())
    aList = [[0 for _ in range(B)] for _ in range(A+1)]
    for i in range(A+1):
        for j in range(B):
            if i == 0:
                aList[i][j] = j+1
            else:
                if j == 0:
                    aList[i][j] = 1
                else:
                    aList[i][j] = aList[i][j-1] + aList[i-1][j]

    print(aList[A][B-1])
