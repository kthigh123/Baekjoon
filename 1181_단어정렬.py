import sys

input_num = sys.stdin.readline

list = []
for _ in range(int(input_num())):
    text = input_num().strip()
    list.append([len(text), text])
    
list.sort()

for i in range(len(list)):
    if(i != 0):
        if(list[i][1] != list[i-1][1]):
            print(list[i][1])
    else:
        print(list[i][1])


