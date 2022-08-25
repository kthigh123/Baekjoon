import sys

arr = [False, False] + [True]*9999

for i in range(2, int(len(arr)**0.5)+1):
  if arr[i]:
    for j in range(2*i, len(arr), i):
      arr[j] = False

inputNum = int(sys.stdin.readline())
for _ in range(inputNum):
  inputNum2 = int(sys.stdin.readline())
  for i in range(inputNum2//2, 0, -1):
    if arr[i] and arr[inputNum2-i]:
      print(f"{i} {inputNum2-i}")
      break