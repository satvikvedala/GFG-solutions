#With O(n) memory
def calculate (arr, n) : 
    #Complete the function
    ma = 0
    res = 0
    for item in arr:
        ma = max(ma,item)
    temp = [0]*(ma+1)
    for item in arr:
        temp[item]+=1
    for item in temp:
        if item>1:
            res += ((item)*(item-1))//2
    return res
