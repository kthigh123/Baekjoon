import sys

count = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
a = sys.stdin.readline().strip()

for i in count:
    a = a.replace(i, " ")

print(len(a))

# A = "house"
# A = A.replace("ou", "i")
# print(A)