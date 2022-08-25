import sys;

inputSetting = sys.stdin.readline

inputNum = int(inputSetting())

def hanoi(N, a, b, c):
    if N == 1:
        print(1, a, c)
    else:
        hanoi(N-1, a, c, b)
        print(2, a, c)
        hanoi(N-1, b, a, c)
sum=1
for _ in range(inputNum-1):
    sum = sum*2+1
print(sum)

hanoi(inputNum, 1, 2, 3)





