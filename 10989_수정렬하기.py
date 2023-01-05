# 답지봄 => 다음에 한 번 더 풀어볼 것
import sys

a = [0]*10001
for i in range(int(sys.stdin.readline())):
    a[int(sys.stdin.readline())] += 1

for i in range(10001):
    if(a[i] != 0):
        for _ in range(a[i]):
            print(i)