class Solution:
    def generateCode(self, n):
        # Code here
        arr = ['0','1']
        i = 2
        while i<=n:
            for j in range(len(arr)-1,-1,-1):
                arr.append(arr[j])
            m = len(arr)
            for k in range(m//2):
                arr[k] = '0'+arr[k]
            for l in range(m//2,m):
                arr[l] = '1'+arr[l]
            i+=1
        return arr
