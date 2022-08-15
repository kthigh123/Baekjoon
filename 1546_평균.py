num_input = int(input())

A = list(map(int, input().split()))
B = max(A)
C = 0

for i in range(len(A)):
    A[i] = A[i] / B * 100

for i in A:
    C += i

print(C/len(A))
