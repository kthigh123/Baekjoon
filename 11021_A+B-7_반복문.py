import sys

custom_input = sys.stdin.readline

num = int(custom_input().strip())
for i in range(num):
    a, b = map(int, custom_input().split())
    print(f"Case #{i+1}: {a+b}")
