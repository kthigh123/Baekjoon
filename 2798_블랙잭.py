import sys;

inputSetting = sys.stdin.readline

num1, num2 = map(int, inputSetting().split())
arr = list(map(int, inputSetting().split()))
jack = 0

for i in range(len(arr)):
    if len(arr)-i > 2:
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                total = arr[i]+arr[j]+arr[k]
                if total <= num2 and total > jack:
                    jack = total

print(jack)