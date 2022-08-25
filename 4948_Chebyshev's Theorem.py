import sys
NUM = 123456
arr = [False, False]+[True]*(NUM*2)
for i in range(2, int(NUM*2**0.5)+1):
  if arr[i]:
    for j in range(2*i, NUM*2+1, i):
      arr[j] = False
      
while(True):
  inputNum = int(sys.stdin.readline().strip())
  if inputNum == 0:
    break
  total = 0
  for i in range(inputNum+1, 2*inputNum+1):
    if arr[i]:
      total += 1
  print(total)