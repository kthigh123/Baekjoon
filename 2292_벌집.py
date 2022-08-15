# 1, 6, 12, 18, 24
# 공차 6인 계차  3n^2 + 3n + 1 공식을 따른다

A = int(input())
i = 0

while A > (3*i*i + 3*i + 1):
    i += 1

print(i+1)
    


