class Solution:
    def maximizeSum(self, a, n, k):
        # Your code goes here
        a = sorted(a)
        min_index = 0
        mi = float("inf")
        for i in range(n):
            if a[i]<0 and k>0:
                a[i] = -1*a[i]
                k-=1
            if a[i]<mi:
                mi = a[i]
                min_index = i
        if k>0:
            temp = k%2
            if temp == 1:
                a[min_index] = -1*a[min_index]
        su = 0
        for item in a:
            su+=item
        return su
