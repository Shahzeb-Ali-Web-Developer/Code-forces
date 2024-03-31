for i in range(int(input())):
    n = int(input())

    height = 0
    width = 0

    for j in range(n):
        a, b = map(int, input().split())

        if a > b:
            width += b
            if a > height:
                height = a

        else:
            width += a
            if b > height:
                height = b

    print(2 * (height + width))