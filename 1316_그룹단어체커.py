import sys

custum_input = sys.stdin.readline

N = int(custum_input())
check = []
total = 0
isTrue = 0

for _ in range(N):
    S = list(map(str, custum_input()))
    for i in range(len(S)):
        if i > 0:
            if S[i] == S[i-1]:
                pass
            else:
                if S[i] in check:
                    isTrue = 1
                    break
                else:
                    check.append(S[i])
        else:
            check.append(S[i])
    if isTrue == 0:
        total += 1
    isTrue = 0
    check = []
    
print(total)


