list = []
name = str(input())
length = len(name)
for i in range(length):
    if name[i] not in list:
        list.append(name[i])
if len(list) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")