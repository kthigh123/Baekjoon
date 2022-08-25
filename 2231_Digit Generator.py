inputNum = int(input())
for i in range(1, inputNum+1):
    arr = list(map(str, str(i)))
    sum = i
    for j in arr:
        sum += int(j)
    if inputNum == sum:
        print(i)
        break
    if i == inputNum:
        print(0)