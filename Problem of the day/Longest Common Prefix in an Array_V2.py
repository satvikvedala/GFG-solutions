class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        def func(str1,str2):
            res = ''
            i = 0
            j = 0
            while(i<len(str1) and j<len(str2)):
                if str1[i]!=str2[j]:
                    break
                res+=str1[i]
                i+=1
                j+=1
            return res
                    
        ref = arr[0]
        for i in range(1,n):
            ref = func(ref,arr[i])
        if len(ref)>0:
            return ref
        return -1
