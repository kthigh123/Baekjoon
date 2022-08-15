from operator import index
import string

A = list(map(str, input()))
B = []

for i in string.ascii_lowercase:
    if i in A:
        B.append(A.index(i))
    else:
        B.append("-1")

for i in B:
    print(i, end=" ")