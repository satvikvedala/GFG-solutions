class Solution:
    def countDistinct(self, A, N, K):
        # Code here
        z = 0
        j = K
        hashmap = {}
        dc = 0
        res = []
        for i in range(K):
            if A[i] not in hashmap:
                dc+=1
                hashmap[A[i]] = 1
            else:
                hashmap[A[i]]+=1
        while j<N:
            res.append(dc)
            first = A[z]
            second = A[j]
            hashmap[first]-=1
            if hashmap[first] == 0:
                dc-=1
            if second not in hashmap or hashmap[second] == 0:
                dc+=1
                hashmap[second] = 1
            else:
                hashmap[second]+=1
            z+=1
            j+=1
        res.append(dc)
        return res   
