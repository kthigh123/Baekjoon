A = int(input())
B = list(map(str, input()))

for i in range(len(B)):
    B[i] = int(B[i])

print(sum(B))