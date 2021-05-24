class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,a,size):
        ##Your code here
        max_end_here = float("-inf")
        max_curr_sum = 0
        for i in range(size):
            max_curr_sum += a[i]
            if max_curr_sum<0:
                max_curr_sum = 0
            if max_curr_sum>max_end_here:
                max_end_here = max_curr_sum
        return max_end_here
