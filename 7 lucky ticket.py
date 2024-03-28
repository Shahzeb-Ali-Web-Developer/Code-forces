len = int(input())
if len % 2 != 0:
    print("Input isn't not even")
else:
    ticket = str(input())
    half_one = len // 2
    sum_one = 0
    for i in range(0, half_one):
        n = ticket[i]
        if n == "7" or n == "4":
            sum_one = sum_one + int(n)

    sum_two = 0
    for j in range(half_one, (half_one*2)):
        n = ticket[j]
        if n == "7" or n == "4":
            sum_two = sum_two + int(n)

    if sum_one > 0 and sum_two > 0 and sum_one == sum_two:
        print("YES")
    else:
        print("NO")