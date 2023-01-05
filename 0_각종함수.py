import sys

input_num = sys.stdin.readline

list_num = int(input_num())
print(list_num) #0 입력시 0 출력

a = []
a.append(list(map(int, input_num().split()))) 
print(a) #1 1 입력시 [[1, 1]] 출력
