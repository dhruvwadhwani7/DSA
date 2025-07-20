t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    count = 0
    i = 0
    while i <= n-k :
        if all( a[j] == 0 for j in range(i,i+k)):
            count += 1
            i += k+1
        else:
            i+= k + 1 
    print(count)
    
# div 3 contest Q1 - 17 july 2024