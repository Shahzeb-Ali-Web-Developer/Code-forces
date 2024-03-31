a = int(input())
for i in range(a):
    ans = "Yes"
    l = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    for n in range(l-1):
        if nums[n] < nums[n+1] and nums[n] != nums[n+1]:
            continue
        else:
            ans = "No"
            break
    print(ans)