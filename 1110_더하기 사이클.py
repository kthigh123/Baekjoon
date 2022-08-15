num = int(input())
a = (num % 10)*10+(num % 10 + num // 10)%10
count = 1

while a != num:
    a = (a % 10)*10+(a % 10 + a // 10)%10
    count += 1

print(count)


# 이 문제는 시간 오류가 계속 나왔다. 이유는 if문과 while 1이였다.
# num = int(input())
# a = num
# count = 0

# while 1:
#     if a < 10:
#         a *= 10

#     a = (a % 10)*10+((a % 10)+(int(a / 10)))%10
#     count += 1
#     if a == num:
#         break

# print(count)
# 위는 초기 제출 코드이며, while에 대한 조건이 애매하기에, 쓸데없는 if문이 두 개가 추가되었다.