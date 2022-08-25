def factorial(N: int):
  if N > 1:
    return N*factorial(N-1)
  else:
    return N

inputNum = int(input())
if inputNum == 0:
  print(1)
else:
  print(factorial(inputNum))