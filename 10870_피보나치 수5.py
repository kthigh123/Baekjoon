def fibonachi(N: int):
  if N == 0:
    return 0
  if N == 1:
    return 1
  return fibonachi(N-2)+fibonachi(N-1)

inputNum = int(input())
print(fibonachi(inputNum))