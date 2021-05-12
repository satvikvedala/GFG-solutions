class Solution:
    def sumXOR (self, arr, n) : 
        #Complete the function
        su = 0
        for i in range(32):
            zeros = 0
            ones = 0
            for j in range(n):
                if (arr[j]&(1<<i))> 0:
                    ones+=1
                else:
                    zeros+=1
            su+=ones*zeros*(2**i)
        return su
