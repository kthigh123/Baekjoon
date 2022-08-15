import sys

num_input = sys.stdin.readline

N = list(map(str, num_input()))
total = 0

for i in N:
    if "A" <= i <= "C":
        total += 3
    elif "D" <= i <= "F":
        total += 4
    elif "G" <= i <= "I":
        total += 5
    elif "J" <= i <= "L":
        total += 6
    elif "M" <= i <= "O":
        total += 7
    elif "P" <= i <= "S":
        total += 8
    elif "T" <= i <= "V":
        total += 9
    elif "W" <= i <= "Z":
        total += 10

print(total)