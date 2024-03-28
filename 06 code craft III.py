m = ["January","February","March","April","May","June","July","August","September","October","November","December"]

month = str(input())

index = 0
for i in range(len(m)):
    if m[i] == month:
        index = i

k = int(input())
if k % 12 == 0:
    print(month)
else:
    for i in range(k):
        index += 1
        if index >= 12:
            index = index % 12

    print(m[index])