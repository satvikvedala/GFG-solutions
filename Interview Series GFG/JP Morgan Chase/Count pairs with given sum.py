class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        dic = dict()
        for i in range(n):
            if arr[i] not in dic:
                dic[arr[i]] = 1
            else:
                dic[arr[i]] += 1
        su = 0
        for i in range(n):
            left = arr[i]
            right = k-arr[i]
            if left in dic and right in dic:
                if left == right:
                    su+=(dic[left]*(dic[left]-1))//2
                    dic[left] = 0
                else:
                    su+=(dic[left]*dic[right])
                    dic[left] = 0
                    dic[right] = 0
        return su
