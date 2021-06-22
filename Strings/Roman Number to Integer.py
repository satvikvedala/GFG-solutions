def romanToDecimal(str):
    # code here
    dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    count = 0
    prev = 9999999999
    curr = -1
    for item in str:
        curr = dic[item]
        if curr<=prev:
            count+=curr
        else:
            count-=prev
            curr-=prev
            count+=curr
        prev = curr
    return count
