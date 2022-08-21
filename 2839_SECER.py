inputNum = int(input())
result = -1

if inputNum % 5 == 0:
    print(inputNum/5)
else:
    for i in range(inputNum//5, 0, -1):
        if (inputNum - i*5) % 3 == 0:
            result = i + (inputNum - i*5) // 3
            break
    if result == -1 and inputNum % 3 == 0:
        result = inputNum // 3
    
print(result)

