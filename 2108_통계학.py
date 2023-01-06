import sys

input_num = sys.stdin.readline

num = int(input_num())
a = [0]*num

for i in range(num):
    a[i] = int(input_num())

a.sort()

print(round(sum(a)/num))
print(a[int(num-1)//2])
c = dict()

    
count = 1

for i in range(1, num+1):
    if(i<num):
        if(a[i] == a[i-1]):
            count += 1
        else:
            c[a[i-1]] = count
            count = 1
    if(i == num):
        c[a[i-1]] = count
        
lih = [k for k,v in c.items() if max(c.values()) == v] # 리스트 컴프리헨션 이용

if len(lih) > 1:
    lih.sort()
    print(lih[1])
else:
    print(lih[0])
print(a[-1]-a[0])
# for _ in range(num):
#     j = int(input_num())
#     print(f"{a}+//+{j}")
#     if (j < 0):
#         a[j+9000] += 1 
#     else:
#         a[j] += 1
# for i in range(a):
#     if(a[i] > 5000):
#         b[i] = 
    
# print(sum(b)/num)
# if(num%2==0):
#     print(b[num//2])
# else:
#     print(b[num//2]+1)
# print(a.indx(max(a)))
# print(max(a))

# for i in range(num):
#     j = int(input_num())
#     if(j<0):
#         j+=9000
#     a[i] = j

# m = max(a)
# b = [0]*(max(a)+1)
# result = [0]*num
# for i in range(a):
#     b[a[i]] += 1
# for i in range(1, m+1):
#     b[i] += b[i-1]
# for i in range(b):
#     result[] 


    

