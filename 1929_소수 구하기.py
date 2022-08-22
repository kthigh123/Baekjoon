import math

M, N = map(int, input().split()) 

sosu = [False, False] + [True]*N
for i in range(2, int(math.sqrt(N)+1)):
    if sosu[i]:
        for j in range(2*i, len(sosu), i):
            sosu[j] = False

sosuNum = [i for i in range(M, N+1) if sosu[i]]
for i in sosuNum:
    if i >= M:
        print(i)
    if i >N:
        break
