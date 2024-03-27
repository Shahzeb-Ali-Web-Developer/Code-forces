# program kaa kaam : agr input odd hogi to just "-1" print krdega
# otherwise even input ki surat mn ek pattern print kryga jo k kuch is trha sy hoga : see below

# 2 1 4 3 6 5 8 7 (n) (n-1)         <----- yahan "n" input value h jo user dega (or ye even hai).

n = int(input())

if n % 2 == 1:
    print(-1)
else:
    for i in range(1, n+1, 2):
        print(i+1, i, end=" ")
