inputNum = int(input())

arr = [False, False]+[True]*inputNum

for i in range(2, int(inputNum**0.5)+1):
    if arr[i]:
        for j in range(2*i, len(arr), i):
            arr[j] = False

sosu = [i for i in range(len(arr)) if arr[i]]

i = 0
while(True):
    if inputNum == 1:
        break
    if inputNum % sosu[i] == 0:
        print(sosu[i])
        inputNum //= sosu[i]
    else:
        i += 1

