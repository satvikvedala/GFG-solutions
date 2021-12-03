def minSwap (arr, n, k) : 
    #Complete the function
    cnt = 0
    for i in range(n):
        if arr[i]<=k:
            cnt+=1
    i = 0
    ans = 0
    for j in range(i,cnt):
        if arr[j]>k:
            ans+=1
    res = float("inf")
    i = 0
    j = cnt
    while(j<n):
        res = min(res,ans)
        if arr[i]>k:
            ans-=1
        i+=1
        if arr[j]>k:
            ans+=1
        j+=1
    ans2 = 0
    for c in range(i,j):
        if arr[c]>k:
            ans2+=1
    res = min(res,ans)
    return res
