def findZeroes(arr, n, m) :
    # code here
    wl = 0
    wr = 0
    count = 0
    minLen = 0
    while wr<n:
        if count<=m:
            if arr[wr] == 0:
                count+=1
            wr+=1
        if count>m:
            if arr[wl] == 0:
                count-=1
            wl+=1
        if (wr-wl)>minLen and count<=m:
            minLen = (wr-wl)
    return minLen
