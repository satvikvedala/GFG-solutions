class Solution:
    def getOddOccurrence(self, arr, n):
        # code here 
        ans = 0
        for i in range(n):
            ans = ans^arr[i]
        return ans
