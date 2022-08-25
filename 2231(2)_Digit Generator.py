# 이 문제는 for문의 반복을 최소화해야하는 문제이다.
# for문의 최소값에 집중을 해야하는데, ssum은 inputNum과 각자리 수의 합이여서
# ssum의 최소 시작값은 inputNum에서 9*자리수를 뺀 값이 될 것이다
# (1의 자리 및 18이하 제외).

inputNum = int(input())
A = inputNum-(len(list(map(int,str(inputNum))))*9)

for i in range(A if A>0 else 1, inputNum+1): 
    ssum = sum(map(int, str(i))) 
    ssum += i
    if inputNum == ssum:
        print(i)
        break
    if i == inputNum:
        print(0)