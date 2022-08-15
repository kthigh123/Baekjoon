def hansu(a):
    num = 0
    for i in range(1, a+1):
        if i < 100:
            num += 1
        else:
            if (i//100 - i%100//10) == (i%100//10 - i%10):
                num +=1
    return num

A = int(input())
print(hansu(A))

