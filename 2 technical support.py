# Only Capital letter supported
for i in range(int(input())):
    length = int(input())
    conv = str(input())
    q = 0
    for j in range(length):
        if conv[j] == "Q":
            q += 1
        elif conv[j] == "A":
            q -= 1
            if q < 0:
                q = 0
    if q <= 0:
        print("Yes")
    else:
        print("No")