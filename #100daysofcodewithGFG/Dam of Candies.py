class Solution:
    def maxCandy(self, height, n): 
        # Your code goes here
        i = 0
        j = n-1
        maxarea = 0
        while i<j:
            maxarea = max(maxarea,(j-i-1)*(min(height[i],height[j])))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return maxarea
