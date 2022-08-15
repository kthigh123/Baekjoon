import sys

num_input = sys.stdin.readline

N = num_input().strip()
N = list(map(str, N.upper()))
N.sort()
total = {}
temp = 0
result = []

for i in range(len(N)):
    if i+1 == len(N):
        temp += 1
        total[N[i]] = temp
        temp = 0      
    elif N[i] == N[i+1]:
        temp +=1
    else:
        temp += 1
        total[N[i]] = temp
        temp = 0
for i in total.values():
    if i > temp:
        temp = i

for key, value in total.items():
    if value == temp:
        result.append(key)

if len(result) == 1:
    print(result[0])
else:
    print("?")

