import sys

custum_input = sys.stdin.readline

selectNum = int(custum_input())
total = 0
A = list(map(int, custum_input().split()))
sosu = [i for i in range(2, max(A)+1)] #한 줄씩 입력해서 리스트에 저장

for i in range(2, max(A)):
    if i in sosu:
        for j in sosu:
            if j > i and j % i == 0:
                sosu.remove(j)

for i in A:
    if i in sosu:
        total += 1
    
print(total)
