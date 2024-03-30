n = int(input())
ans = ""
for i in range(1, n+1):
    if i != 1:
        ans += "that "
    if i % 2 != 0:
        ans += "I hate "
    if i % 2 == 0:
        ans += "I love "
ans += "it"

print(ans)
