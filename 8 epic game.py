import math

a, b, n = map(int, input().split())
A_gcd = 0
B_gcd = 0
while n != 0:

    # 1st player turn (simons)

    gcd = math.gcd(a, n)
    n = n - gcd

    # below is a check if the stones in heap ended. if this condition meets true, the program will end and
    # current player (simon) will win bcz heap ended in his turn.
    # if it doesn't meet, program will continue to 2nd player turn bcz there are still stones in heap.

    if n == 0:
        print("0")
        break

    # 2nd player turn (Antisimon)

    B_gcd = math.gcd(b, n)
    n = n - B_gcd

    # below is a check if the stones in heap ended. if this condition meets true, the program will end and
    # current player (antisimon) will win bcz heap ended in his turn.
    # if it doesn't meet, program will continue to 1st player turn (new iteration)
    # bcz there are still stones in heap.

    if n == 0:
        print("1")
        break