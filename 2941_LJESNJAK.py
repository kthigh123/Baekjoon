import sys

custum_input = sys.stdin.readline

A = list(map(str, custum_input()))
total = 0

for i in range(len(A)-1):
    if i >= 1:
        if A[i] == "=" and A[i-1] == "z":
            if i >= 2: 
                if A[i-2] == "d":
                    total -= 1
            else:
                pass
        elif A[i] == "=" and A[i-1] in ["c", "s", "z"]:
            pass
        elif A[i] == "-" and A[i-1] in ["c", "d"]:
            pass
        elif A[i] == "j" and A[i-1] in ["l", "n"]:
            pass
        else:
            total += 1
    else:
        total += 1

print(total)
    


