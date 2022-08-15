import sys


num_input = int(input())

for _ in range(num_input):
    A = list(map(int, sys.stdin.readline().strip().split()))
    avg = (sum(A)-A[0]) / A[0]
    total = 0
    for i in range(len(A)):
        if i == 0:
            continue
        elif A[i] > avg:
            total += 1
    print("{:.3f}%".format(total/A[0]*100))
                                        