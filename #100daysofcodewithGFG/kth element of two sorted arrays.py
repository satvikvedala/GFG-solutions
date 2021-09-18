class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        i = 0
        j = 0
        arr = []
        while i<n and j<m:
            if arr1[i]<arr2[j]:
                arr.append(arr1[i])
                i+=1
            else:
                arr.append(arr2[j])
                j+=1
        while i<n:
            arr.append(arr1[i])
            i+=1
        while j<m:
            arr.append(arr2[j])
            j+=1
        return arr[k-1]
