import sys

input_num = sys.stdin.readline

num = int(input_num())
a = []

for i in range(1, num+1):
    if(i != 1):
        a.append(int(input_num()))
        for j in range(i-1, 0, -1):
            if(a[j-1] > a[j]):
                temp = a[j-1]
                a[j-1] = a[j]
                a[j] = temp
            else:
                break
    else:
        a.append(int(input_num()))
        
for i in a:
    print(i)
        
# for i in range(num):
#     a.append(int(input_num()));
# a.sort()
# for i in a:
#     print(i)