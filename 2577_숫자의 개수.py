A = [int(input()) for _ in range(3)] #한 줄씩 입력해서 리스트에 저장
B = list(map(int, str(A[0]*A[1]*A[2]))) # str()을 한 글자씩 int형으로 나누어 list로 저장
#B = [int(a) for a in str(A[0]*A[1]*A[2])] 도 같은 결과를 낸다. 똑같은 원리로 str()을 한 글자씩 B리스트에 저장하니깐.

for i in range(10):
    print(B.count(i))

