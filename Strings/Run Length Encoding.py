def encode(arr):
    # Code here
    item = arr[0]
    count = 1
    st = ''
    for i in range(1,len(arr)):
        if arr[i] == item:
            count+=1
        else:
            st = st+item+str(count)
            item = arr[i]
            count = 1
    st+=item+str(count)
    return st
