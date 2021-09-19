class Solution:
    def MedianOfArrays(self, array1, array2):
            #code here
            import math
            arr = []
            i = 0
            j = 0
            while i<len(array1) and j<len(array2):
                if array1[i]<array2[j]:
                    arr.append(array1[i])
                    i+=1
                else:
                    arr.append(array2[j])
                    j+=1
            while i<len(array1):
                arr.append(array1[i])
                i+=1
            while j<len(array2):
                arr.append(array2[j])
                j+=1
            mid = len(arr)//2
            if len(arr)%2!=0:
                return arr[mid]
            else:
                ans = (arr[mid]+arr[mid-1])/2
                if math.floor(ans) == ans:
                    return int(ans)
                return ans
