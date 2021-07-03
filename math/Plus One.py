class Solution:
    def increment(self, arr, N):
        # code here 
        carry = 0
        i = len(arr)-1
        while i>=0:
            if i == len(arr)-1:
                arr[i] = arr[i]+1
            else:
                arr[i] = arr[i]+carry
            if arr[i]>9:
                arr[i] = 0
                carry = 1
            elif arr[i]<=9:
                carry = 0
            i-=1
        if carry == 1:
            return [1]+arr
        return arr
