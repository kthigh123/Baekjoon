import sys

input_num = sys.stdin.readline

list_num = input_num()

a = [[0 for j in range(100)] for i in range(100)]
e = 0
for i in range(int(list_num)):
    c, d = map(int, input_num().split())
    for j in range(10):
        for k in range(10):
            if(a[c+j][d+k] == 0):
                a[c+j][d+k] = 1
                e += 1
    
print(e)
