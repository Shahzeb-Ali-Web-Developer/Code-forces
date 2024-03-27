attempt = 0
for i in range(int(input())):
    a, b, c = input().split()
    if int(a) + int(b) + int(c) >= 2:
        attempt += 1
print(attempt)