class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		if n == 1:
		    return arr[0]
		ma = 1
		mi = 1
		res = float("-inf")
		for i in range(n):
		    if arr[i]>0:
		        ma = ma*arr[i]
		        mi = mi*arr[i]
		    elif arr[i] == 0:
		        ma = 1
		        mi = 1
		    else:
		        temp = ma*arr[i]
		        ma = max(1,arr[i]*mi)
		        mi = temp
		    res = max(res,ma)
	    return res
