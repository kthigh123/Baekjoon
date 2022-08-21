## 이거는 시간적인 단축이 들어가는 코드이다.

arr = [False, False] + [True] * 9999 #0과 1은 소수가 아니다.
for i in range(2, 101): #sqrt(N)이하의 소수만 나눠봐도 판별 가능
    if arr[i]:
        for j in range(i * 2, len(arr), i): #배수를 전부 false로
            arr[j] = False

m = int(input())
n = int(input())
nums = [i for i in range(m, n+1) if arr[i]]
print(sum(nums)if len(nums) else -1)
print(min(nums) if len(nums) else '')