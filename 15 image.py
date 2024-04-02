for i in range(int(input())):
    p1 = str(input())
    p2 = str(input())
    list = []
    for p in range(2):
        if p1[p] not in list:
            list.append(p1[p])
    for p in range(2):
        if p2[p] not in list:
            list.append(p2[p])

    pixel = list[0]
    moves = 0
    for i in range(len(list)):
        if list[i] != pixel:
            moves += 1

    print(moves)