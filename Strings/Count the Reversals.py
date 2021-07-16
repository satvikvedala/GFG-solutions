def countRev (s):
    # your code here
    if len(s)%2!=0:
        return -1
    open = 0
    count = 0
    for item in s:
        if item == '{':
            open+=1
        elif open>0:
            open-=1
        else:
            open+=1
            count+=1
    return count+open//2
