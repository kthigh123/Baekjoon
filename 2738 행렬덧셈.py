import sys

input_num = sys.stdin.readline
n, m = map(int, input_num().strip().split())
a = []
for _ in range(n*2):
    a.append(list(map(int, input_num().strip().split())))
    
for i in range(n):
    for j in range(m):
        print(f"{a[i][j]+a[n+i][j]} ", end="")
    print("")


