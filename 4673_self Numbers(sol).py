def self_number():
    A = [0] * 11000
    
    for i in range(1, 9999):
        A[(i+i//1000+ i%1000 //100 + i%100 //10 + i%10)] = 1
    
    return A

n = self_number()
for i in range(1, 10000):
    if n[i] == 0:
        print(i)

#이 코드는, 배열을 기존 두 개(+ su숫자배열 1개) 쓰던 것에서 하나 쓰는 것으로 확 줄였다.
#self number는 0, 이외에는 1로 처리해 처리 시간을 10배 줄인코드.