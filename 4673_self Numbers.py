def self_number():
    A = []
    n = []

    for i in range(10000):
        su = list(map(str, str(i)))
        do = 0
        for j in su:
            do += int(j)
        if i+do < 10000:
            n.append(i+do)
    for i in range(10000):
        if i not in n:
            A.append(i)
    return A

A = self_number()
for i in A:
    print(i)
