num_input = int(input())

for _ in range(num_input):
    total = 0
    temp = 0
    A = list(map(str, input()))
    for i in range(len(A)):
        if A[i] == 'O':
            temp += 1
            total += temp
        else:
            temp = 0
    print(total)
            


