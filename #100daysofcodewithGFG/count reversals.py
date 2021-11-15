def countRev (s):
    # your code here
    op = 0
    cl = 0
    count=0
    for item in s:
        if item == '{':
            op+=1
        else:
            cl+=1
        if cl>op:
            count+=1
            cl-=1
            op+=1
    temp = op-cl
    if temp%2!=0:
        return -1
    return count+temp//2
