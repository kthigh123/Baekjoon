import sys

num_input = sys.stdin.readline

count = ["ABC", "DEF", "GHI", "JKL",\
     "MNO", "PQRS", "TUV", "WXYZ"]
# 줄이 너무 길어서 \으로 줄을한줄 띄움, 
# count에 문자들을 저장해둔다.

N = list(map(str, num_input()))
total = 0

for i in N:
   for j in count:
    if i in list(j):
        total += (count.index(j)+3)

# count를 돌면서
print(total)