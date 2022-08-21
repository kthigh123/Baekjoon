import math


M = int(input())
N = int(input())

sosu = [i for i in range(2, N+1)] #자꾸 소수가 2부터인걸 까먹는다 [i for i in range(1, N+1)] << 이거때문에 오류남

for i in range(2, int(math.sqrt(N)+1)):
    if i in sosu:
        for j in sosu:
            if j > i and j % i == 0:
                sosu.remove(j)

for i in sosu[:]:
    if i < M:
        sosu.remove(i)

if len(sosu) == 0:
    print(-1)
else:
    print(sum(sosu))
    print(min(sosu))
