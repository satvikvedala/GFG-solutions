class Solution:
    def querySum(self, n, arr, q, queries):
        # code here
        sum_arr = [0]*n
        left_sum = [0]*n
        right_sum = [0]*n
        left_sum[0] = 0
        sum_arr[0] = arr[0]
        for i in range(1,n):
            sum_arr[i] = sum_arr[i-1]+arr[i]
            left_sum[i] = sum_arr[i]-arr[i]
        for i in range(n):
            right_sum[i] = sum_arr[-1]-sum_arr[i]
        i = 0
        j = 1
        res = []
        while j<len(queries):
            x = queries[i]
            y = queries[j]
            res.append(sum_arr[-1]-left_sum[x-1]-right_sum[y-1])
            i+=2
            j+=2
        return res
