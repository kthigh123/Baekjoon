# import sys

# custum_input = sys.stdin.readline

# A, B, C = map(int, custum_input().split())
# total = 1
# temp = 0

# while C > temp + A:
#     temp += A - B
#     total += 1

# print(total) 
# 시간 초과


import sys

custum_input = sys.stdin.readline

A, B, V = map(int, custum_input().split())

if V - A == 0:
    total = 0
elif A - B > V - A :
    total = 1
else:
    if (V-A) % (A-B) == 0:
        total = (V-A)//(A-B)
    else:
        total = (V-A) // (A-B) + 1

print(total+1)
