for j in range(int(input())):
    a, b, c = map(int, input().split())

    t = a - 1
    t1 = (c - b)
    if t1 < 0:
        t1 = -t1
    t1 = t1 + (c - 1)

    if t < 0:
        t = 0

    if t < t1:
        print(1)
    if t > t1:
        print(2)
    if t == t1:
        print(3)