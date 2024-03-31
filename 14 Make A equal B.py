for i in range(int(input())):
    length = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    one_a, one_b = 0, 0
    mismatch = 0

    for i in range(length):
        if a[i] == 1:
            one_a += 1
        if b[i] == 1:
            one_b += 1

        if a[i] != b[i]:  # finds mis match cases in both list corresponding entries
            mismatch += 1

    diff = abs(one_a - one_b)  # diff of entries between lists : how many entries in l1 that are not in l2

    if a == b:
        print(0)
    elif one_a == one_b:  # case when only re-arrange is required
        print(1)
    elif diff == mismatch:  # case when only replace is required, prints how many replaces required
        print(diff)
    else:  # worst case : when both operations, re-arrange and replace are required
        print(diff + 1)
