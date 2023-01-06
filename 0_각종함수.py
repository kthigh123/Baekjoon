import sys

input_num = sys.stdin.readline

list_num = int(input_num())
print(list_num) #0 입력시 0 출력

a = []
a.append(list(map(int, input_num().split()))) 
print(a) #1 1 입력시 [[1, 1]] 출력

#카운팅 정렬
def counting(arr):
    m = max(arr)
    C = [0] * (m + 1)
    for a in arr:
        C[a] += 1
    for i in range(1, m + 1):
        C[i] += C[i - 1]
    result = [0] * len(arr)
    for a in arr:
        result[C[a] - 1] = a
        C[a] -= 1
    return result
a = [3, 1, 2, 5, 4, 6]
b = [6, 5, 4, 3, 2, 1]
c = [5, 5, 3, 3, 1, 1]