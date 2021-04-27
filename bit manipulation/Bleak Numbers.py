class Solution:
	def is_bleak(self, n):
		# Code here
		import math
		def func2(n):
		    return math.floor(math.log(n)/math.log(2))
		def func(x):
		    count = 0
		    while x>0:
		        x&=(x-1)
		        count+=1
		    return count
		for i in range(n - func2(n),n):
		    if i+func(i) == n:
		        return 0
		return 1
