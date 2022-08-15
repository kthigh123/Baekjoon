# 1/1을 2, 2/1을 3과 같이 분모 분자의 합으로 본다면 대각선은 공차가 1인 계차수열이다.

A = int(input())

i = 0

while A > (i*(i+1)//2):
    i += 1

c = A - ((i-1)*i//2) - 1
if i % 2 == 0:
    print(f"{c+1}/{i-c}")
else:
    print(f"{i-c}/{c+1}")