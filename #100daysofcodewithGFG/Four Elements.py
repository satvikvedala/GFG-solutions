def find4Numbers( A, n, X):
    # return true or false
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                temp1 = True if X-(A[i]+A[j]+A[k]) in A else False
                temp2 = True if X-(A[i]+A[j]+A[k]) != A[i] else False
                temp3 = True if X-(A[i]+A[j]+A[k]) != A[j] else False
                temp4 = True if X-(A[i]+A[j]+A[k]) != A[k] else False
                if temp1 and temp2 and temp3 and temp4:
                    return 1
    return 0
