class Solution:
    def isKSortedArray(self, arr, n, k): 
        #code here.
        temp = arr.copy()
        temp = sorted(temp)
        dic1 = {}
        dic2 = {}
        for i in range(len(arr)):
            dic1[arr[i]] = i
        for i in range(len(temp)):
            dic2[temp[i]] = i
        for item in arr:
            if abs(dic1[item] - dic2[item])>k:
                return 'No'
        return 'Yes'
