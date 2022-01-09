class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        refer = ''
        refer_len = float('inf')
        for item in arr:
            if len(item)<refer_len:
                refer = item
                refer_len = len(item)
        #print(refer)
        max_ln = float("inf")
        for item in arr:
            max_ln = min(max_ln,len(item))
        arr1 = [0]*max_ln
        #print(arr1)
        for i in range(n):
            for j in range(refer_len):
                if arr[i][j] == refer[j]:
                    arr1[j]+=1
        #print(arr1)
        ans = ''
        for i in range(len(arr1)):
            if arr1[i] == n:
                ans+=refer[i]
            else:
                break
        if len(ans)>0:
            return ans
        return -1
